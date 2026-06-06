from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id=models.CharField(max_length=20 , unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=10)
    department=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    salary=models.DecimalField(max_length=100 , decimal_places=2,max_digits=10)
    joining_date=models.DateField()
    def __str__(self):
        return self.first_name

