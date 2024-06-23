from django.db import models

# Create your models here.
class Employees(models.Model):
    name=models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    salary=models.CharField(max_length=30)
    bonus=models.CharField(max_length=30)
    
    class Meta:
        db_table='employees'