from django.db import models


# Create your models here.



class Registro(models.Model):
    n_do_protocolo = models.CharField(max_length=100)
    apresentante = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
