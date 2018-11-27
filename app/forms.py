from django import forms
from app.models import User,UserFile
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea, EmailField


class NewUserForm(forms.ModelForm):
    
    class Meta: 
        model=User
        exclude=['submission_Time',]
        labels = {
          

        }
        widgets = {
            'notes': Textarea(attrs={'class': 'form-control form-control-sm','placeholder':'Pleae specify how many files are attached as well as anything that you want to tell us!'}),
            

        }

class NewUserFileForm(forms.ModelForm):

    class Meta: 
        model= UserFile
        fields = ['submission_Box']
        widgets = {
           'submission_Box': forms.ClearableFileInput(attrs={'multiple':True})
        }

