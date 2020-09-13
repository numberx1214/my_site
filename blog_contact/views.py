from django.shortcuts import render, redirect

# Create your views here.
from blog_contact.forms import CreateContactForm
from blog_contact.models import Contact


def contact(request):
    contact_form = CreateContactForm(request.POST or None)

    if contact_form.is_valid():
        name = contact_form.cleaned_data.get('name')
        email = contact_form.cleaned_data.get('email')
        message = contact_form.cleaned_data.get('message')
        Contact.objects.create(name=name, email=email, message=message, is_read=False)
        contact_form = CreateContactForm()
    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact.html', context)
