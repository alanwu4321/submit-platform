from django import forms
from app.models import User
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea, EmailField

class NewUserForm(forms.ModelForm):
    
    class Meta: 
        model=User
        exclude=['submission_Time',]
        labels = {
          

        }
        widgets = {
            'notes': Textarea(attrs={'class': 'form-control form-control-sm'}),

        }


