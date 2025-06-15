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
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        base_class = (
            'shadow appearance-none border rounded w-full py-2 px-3 '
            'text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
        )
        error_class = ' border-red-500 focus:border-red-500 focus:ring-red-500'

        # Set base classes and placeholders for all fields
        self.fields['username'].widget.attrs['class'] = base_class
        # self.fields['username'].widget.attrs['placeholder'] = 'Username'

        self.fields['password1'].widget.attrs['class'] = base_class
        # self.fields['password1'].widget.attrs['placeholder'] = 'Password'

        self.fields['password2'].widget.attrs['class'] = base_class
        # self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

        # Append error classes if the field has errors
        for field_name in self.errors:
            existing_classes = self.fields[field_name].widget.attrs.get('class', '')
            if error_class.strip() not in existing_classes:
                self.fields[field_name].widget.attrs['class'] = existing_classes + error_class
