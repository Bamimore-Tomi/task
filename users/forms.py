from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=150)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc  = forms.BooleanField(required=False)