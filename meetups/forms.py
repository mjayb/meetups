from django import forms
#from django.contrib.auth.models import user
#from django.contrib.auth.forms import UserCreationForm
from .models import Participant, User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea, TextInput



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields=['email']
        widgets = {
           
            'email':TextInput(
                attrs={
                    "placeholder": "Enter your email",
                    "class":"form-control"
                }
            )
        }


class MyUserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username', 'email', 'password1', 'password2', ]
        widgets = {
            
        
            'email':TextInput(
                attrs={
                   "placeholder": "Enter email",
                   "class":"form-control"
                }
            ),
            'username':TextInput(
                attrs={
                   "placeholder": "Enter username",
                   "class":"form-control"
                }
            ),
            
            
         }

class Profile(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'username', 'email'] 
        widgets = {
            
            
            
            'email':TextInput(
                attrs={
                   "placeholder": "Enter your email",
                   "class":"form-control"
                }
            ),
            'username':TextInput(
                attrs={
                   "placeholder": "Enter location name",
                   "class":"form-control"
                }
            )
           
            
        }       
