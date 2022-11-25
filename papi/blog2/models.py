from ast import mod
from django.db import models

# Create your models here.
class Datos(models.Model):

    

    x1 = models.FloatField()
    x2 = models.TextField()
    x3 = models.FloatField()
    x4 = models.FloatField()
    def __str__(self):
        return str(self.x1) +' , '+str(self.x2) +' , '+str(self.x3) +' , '+str(self.x4)