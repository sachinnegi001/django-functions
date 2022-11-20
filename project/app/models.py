from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
   user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
   file=models.ImageField(upload_to="media/" ,null=True) 
   dateofbirth=models.DateField(null=True ,blank=True)
   phonenumber=models.CharField(null=True,max_length=12)
   email=models.CharField(max_length=200,null=True)
   age = models.CharField(max_length=100,null=True)
   
   
   def __str__(self):
       return str(self.user)
   
   