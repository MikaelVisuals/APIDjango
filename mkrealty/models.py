from django.db import models


class Realty(models.Model):
    TYPE_CHOICES = (("Sale", "SALE"), ("Rent", "RENT"))
    STATUS_CHOICES = (("Available", "AVAILABLE"), ("Sold", "SOLD"), ("Rented", "RENTED"))

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='Sale')
    price = models.FloatField(default=0)
    location = models.CharField(max_length=200)
    info = models.CharField(max_length=500)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Available')

    def __str__(self):
        return self.name + ' ' + self.type + ' ' + str(self.price) + ' ' + self.location + ' ' + self.info
