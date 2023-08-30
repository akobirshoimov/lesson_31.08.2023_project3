from django.db import models
from datetime import datetime

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=50,default = ' ')
    date_of_birth = models.DateTimeField(default = datetime.now)
    
    def __str__(self) -> str:
        return self.name 

class Teachers(models.Model):
    name = models.CharField(max_length=60,default = ' ')
    date_of_birth = models.DateTimeField(default = datetime.now)
    
    def __str__(self) -> str:
        return self.name 
    

