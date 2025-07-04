from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'profile_picture', 'username', 'email', 
            'user_type', 'address_line1', 'city', 'state', 'pincode'
        )
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2