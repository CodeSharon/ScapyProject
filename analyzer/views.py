from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import CaptureRequest
from scapy.all  import get_if_list
from django.shortcuts import render
from scapy.all import *
from django.http import HttpResponse 

#Authentification pour deux types d'utilisateurs 
def login_view(request):
    error_message = None 
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            # l'utilisateur existe il se connecte automatiquement
            login(request, user)
            if user.is_staff:
                # Redirect expert users to the capture request list
                return redirect('capture_request_list')
            else:
                return redirect('request_form') 
        else:
            # L'utilisateur n'existe pas en base il est crée
            role = 'user'
            user = User.objects.create_user(username=username, password=password)
            user.role = role
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('request_form') 
    return render(request, 'login.html', {'error_message': error_message})

@login_required
def request_view(request):
    interfaces = get_if_list()
    existing_capture = None

    if request.method == 'POST':
        nom_demande = request.POST['nom_demande']
        selected_interface = request.POST['selected_interface']
        count = request.POST['count']
        filter_value = request.POST['filter']

        # Vérifie si une demande similaire existe
        existing_capture = CaptureRequest.objects.filter(
            nom_demande=nom_demande,
            selected_interface=selected_interface,
            filter=filter_value,
            is_running=True
        ).first()

        
        # Crée une instance de CaptureRequest et enregistre en base de données
        capture_request = CaptureRequest.objects.create(
            nom_demande=nom_demande,
            selected_interface=selected_interface,
            count=count,
            filter=filter_value
        )

        return render(request, 'request_submitted.html', {'capture_request': capture_request,'existing_capture': existing_capture})

    return render(request, 'request_form.html', {'interfaces': interfaces})

# recuperation la demande
def capture_requests_list(request):
    capture_requests = CaptureRequest.objects.all()
    return render(request, 'capture_request_list.html', {'captures': capture_requests})

#Lancement d'une capture
def start_capture(request):
    if request.method == 'POST':
        capture_id = request.POST.get('capture_id')
        capture = CaptureRequest.objects.get(pk=capture_id)
       
        selected_interface = capture.selected_interface
        count = capture.count
        filter_value = capture.filter

        packets = sniff(iface=selected_interface, count=count, filter=filter_value)

        # Enregistre les paquets capturés dans un fichier .cap 
        capture_file_path = f'/home/osboxes/network_analyzer/Captures/{capture.nom_demande}.cap'
        wrpcap(capture_file_path, packets)

        capture.is_running = True   
        capture.save()
        
        # Redirige l'expert vers une page de confirmation avec des informations sur la capture
        return render(request, 'capture_started.html', {'capture': capture, 'capture_file_path': capture_file_path})
    else:
        return HttpResponse("Method not allowed", status=405)
    
def capture_started(request, capture_id):
    capture = CaptureRequest.objects.get(pk=capture_id)
    return render(request, 'capture_started.html', {'capture': capture})

#Suppression d'une demande de capture
def delete_capture(request, capture_id):
    capture = CaptureRequest.objects.get(pk=capture_id)
    capture.delete()
    return redirect('capture_request_list')

#Interruption d'une capture 
def stop_capture(request, capture_id):
    capture = CaptureRequest.objects.get(pk=capture_id)
    capture.is_running = False
    capture.save()
    return redirect('capture_request_list')