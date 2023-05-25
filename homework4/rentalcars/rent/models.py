from django.db import models

class Dealership(models.Model):
    name = models.CharField(max_length=160)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=160)
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name

