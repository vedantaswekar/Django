from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    batch = models.CharField(max_length=20)


    def __str__(self):
         return self.name