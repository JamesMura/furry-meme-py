from django import forms
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    confirmPassword = forms.CharField(widget=forms.PasswordInput(), label="Password Confirmation", required=True)

    def clean_confirmPassword(self):
        if self.cleaned_data["confirmPassword"] != self.cleaned_data["password"]:
            raise ValidationError("Passwords do not match")
        return True




