from django.db import models
from django import forms

class resume(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='static/')
# Create your models here.
# class resume(models.Models):
