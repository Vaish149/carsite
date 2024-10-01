from django.db import models

# Create your models here.


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    mileage = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=30)
    num_doors = models.IntegerField()
    seating_capacity = models.IntegerField()


