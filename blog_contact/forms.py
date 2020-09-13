from django import forms
from django.core import validators


class CreateContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',"id": "name", 'placeholder': 'name', }),
        label='name',
        validators=[
            validators.MaxLengthValidator(200, 'your name can not be more than 200 characters')
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "email", "class": "form-control"}),
        label="email address",
        validators=[
            validators.EmailValidator("your email is not valid")
        ]
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "rows": "5",
            "class": "form-control",
            "placeholder": "Message"

        }),
        label="message"
    )
