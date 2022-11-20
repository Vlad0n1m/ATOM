from django.db import models

class Employee(models.Model):
   name = models.CharField(max_length=50) 
   status = models.CharField(max_length=50, default='not_work')
   def __str__(self) -> str:
      return self.name