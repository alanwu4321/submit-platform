from django.db import models
from datetime import datetime    

# Create your models here.

class User(models.Model):
    group_name = models.CharField(max_length=128)
    submission = models.CharField(max_length=128)
    submission_Box = models.FileField(upload_to='uploads/%Y/%m/%d/')
    notes = models.CharField(max_length=128)
    submission_Time = models.DateTimeField(default=datetime.now, blank=True)
    

class Admin (models.Model):
    Project_Name = models.CharField(max_length=128)
    Project_Detail = models.CharField(max_length=128)
    Project_DueDate = models.DateTimeField(default=datetime.now, blank=True)
    Admin_File_Upload = models.FileField(upload_to='uploads/%Y/%m/%d/')