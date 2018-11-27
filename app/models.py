from django.db import models
from datetime import datetime    

# Create your models here.

class User(models.Model):
    group_name = models.CharField(max_length=128)
    submission = models.CharField(max_length=128)
    #submission_Box = models.FileField(upload_to='uploads/%Y/%m/%d/')
    notes = models.CharField(max_length=128)
    submission_Time = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):     #toString method
        return self.group_name + " --- "+ self.submission

class UserFile(models.Model):
    submission_Box = models.FileField(upload_to='uploads/%Y/%m/%d/')
    group = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    submission_Time = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):     #toString method
        return self.group.group_name + " --- " + self.group.submission +" --- "+self.submission_Time.strftime('%Y-%m-%d')

class Admin (models.Model):
    Project_Name = models.CharField(max_length=128)
    Project_Detail = models.CharField(max_length=128)
    Project_DueDate = models.DateTimeField(default=datetime.now, blank=True)
    Admin_File_Upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):     #toString method
        return self.Project_Name