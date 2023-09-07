from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('request_form', views.request_view, name='request_form'),
    path('start_capture', views.start_capture, name='start_capture'),
    path('capture_request_list', views.capture_requests_list, name='capture_request_list'),
    path('capture_started/', views.capture_started, name='capture_started'),
    path('delete_capture/<int:capture_id>/', views.delete_capture, name='delete_capture'),
    path('stop_capture/<int:capture_id>/', views.stop_capture, name='stop_capture'),
]