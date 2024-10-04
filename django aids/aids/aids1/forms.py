from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField(label='your Name',max_length=100)
    email = forms.EmailField(label='your Email')
    message = forms.CharField(widget=forms.Textarea, label='message')
class RegisterForm(UserCreationForm):
    class meta:
        model = User
        fields = ['uername','email','password1','password2']    
  