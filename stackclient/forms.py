from django import forms
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(), required=True, min_length=6)
    confirmPassword = forms.CharField(widget=forms.PasswordInput(), label="Password Confirmation", required=True,
                                      min_length=6)

    def clean_confirmPassword(self):
        if 'password' in self.cleaned_data:
            if self.cleaned_data["confirmPassword"] != self.cleaned_data["password"]:
                raise ValidationError("Passwords do not match.")
            return True




