from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    def __str__(self):
        return self.name
    
    #user = models.OneToOneField(User, on_delete=models.CASCADE)

    seller_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images')