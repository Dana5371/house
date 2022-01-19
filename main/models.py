from django.db import models
from account.models import User

# Create your models here.

class Ad(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='health')
    title = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='ad', blank=True)
    

    def __str__(self):
        return self.title

    
    