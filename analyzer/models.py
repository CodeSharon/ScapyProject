from django.db import models

class CaptureRequest(models.Model):
    nom_demande = models.CharField(max_length=100)
    selected_interface = models.CharField(max_length=100)
    count = models.IntegerField()
    filter = models.CharField(max_length=100)
    is_running = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nom_demande

