from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    salary = models.FloatField()


    def __str__(self):
         return self.name