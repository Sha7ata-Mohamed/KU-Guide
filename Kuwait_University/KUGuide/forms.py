# KUGuide/forms.py
from django import forms
from django.core.exceptions import ValidationError
import re

from .models import Profile


KU_EMAIL_REGEX = re.compile(r"^(?:s\d{7,10}|[a-zA-Z]+(?:[._-][a-zA-Z]+)*)@ku\.edu\.kw$")


class SignInForm(forms.Form):
    email = forms.EmailField(
        label="Kuwait University Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "s123456@ku.edu.kw",
                "pattern": "[A-Za-z0-9._%+-]+@(ku\\.edu\\.kw)",
                "inputmode": "email",
                "autocomplete": "email",
                "class": "form-control",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "class": "form-control"}
        ),
    )
    remember_me = forms.BooleanField(required=False)

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if not KU_EMAIL_REGEX.match(email):
            raise ValidationError(
                "Use KU email like s12345678@ku.edu.kw or name@ku.edu.kw."
            )
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["major", "bio", "profile_picture"]
        widgets = {
            "major": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your major"}
            ),
            "bio": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "placeholder": "Short bio"}
            ),
        }
