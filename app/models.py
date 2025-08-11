from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    
    def __str__(self):
        return self.brand
