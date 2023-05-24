from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=160)
    price = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return self.name
