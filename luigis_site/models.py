from django.conf import settings
from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    id = models.IntegerField(primary_key=True)

    def publish(self):
        self.save()
    
    def itemInfo(self):
        return (str(self.name) + " " + self.description + 
            " $" + str(self.price))
    
    def __str__(self):
        return self.name


class CartItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    id = models.IntegerField(primary_key=True)

    def publish(self):
        self.save()
    
    def itemInfo(self):
        return (str(self.name) + " " + 
            " $" + str(self.price) + " " + self.quantity)
    
    def __str__(self):
        return self.name