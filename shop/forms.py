# shop/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Username',
            })
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Tailwind classes to password fields explicitly
        self.fields['password1'].widget.attrs.update({
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            
        })