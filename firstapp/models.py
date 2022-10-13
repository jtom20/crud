from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class usermember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_address = models.TextField()
    user_gender = models.CharField(max_length=255)
    user_mobile = models.BigIntegerField()
    user_photo = models.ImageField(upload_to='image/', null=True)
    
    def __str__(self):
        return self.user_gender

class course_details(models.Model):
    course_name = models.CharField(max_length=255)
    duration = models.BigIntegerField()
    fee = models.BigIntegerField()
    
    def __str__(self):
        return self.course_name

class student_details(models.Model):
    course = models.ForeignKey(course_details, null=True, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    age = models.IntegerField()
    gender = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=255)
    joining_date = models.DateField()
    image = models.ImageField()
    
    def __str__(self):
        return self.name
    

     