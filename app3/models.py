from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class StudentsModel(models.Model):
    name = models.CharField(max_length=50,default = ' ')
    date_of_birth = models.DateTimeField(default = datetime.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name 

class TeachersModel(models.Model):
    name = models.CharField(max_length=60,default = ' ')
    date_of_birth = models.DateTimeField(default = datetime.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name 
    

