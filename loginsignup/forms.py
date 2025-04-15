# loginsignup/forms.py

from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Enter your last name'}),
            'username': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Enter your username'}),
            'password': forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Enter your password'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        
        return cleaned_data
