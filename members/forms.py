from django import forms
from django.contrib.auth.password_validation import validate_password
from django.utils.safestring import mark_safe
from .models import Member
import logging

logger = logging.getLogger(__name__)

class Registration(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}),
        validators=[validate_password]
    )
    
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'phone_num', 'user_name', 'password']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'phone_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User name'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if self.errors.get(field_name):
                field.widget.attrs['class'] += ' is-invalid'

        # Append the icon to the password field
    #     self.fields['password'].widget = forms.PasswordInput(
    #         attrs={'class': 'form-control'}
    #     )

    # def as_p(self):
    #     output = ''
    #     for field_name, field in self.fields.items():
    #         if field_name == 'password':
    #             output += '<p>' + str(self[field_name]) + '<i class="bi bi-eye-slash" id="togglePassword"></i></p>'
    #         else:
    #             output += '<p>' + str(self[field_name]) + '</p>'
    #     return mark_safe(output)

