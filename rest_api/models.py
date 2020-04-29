from django.db import models

# Create your models here.
class users(models.Model):  
    User_id = models.CharField(max_length=20)  
    Name = models.CharField(max_length=100)  
    Age = models.IntegerField()  
    Department = models.CharField(max_length=20)  
    Subject = models.TextField(max_length=100)
    def __str__(self):
          return self.Name
