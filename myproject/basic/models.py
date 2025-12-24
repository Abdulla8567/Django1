from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class userProfile(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    city = models.CharField(max_length=100)

class Employee(models.Model):
    emp_name = models.CharField(max_length=150)
    emp_salary = models.IntegerField()
    emp_email=models.EmailField(unique=True)