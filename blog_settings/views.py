from django.shortcuts import render

# Create your views here.
from .models import Setting


def header_setting(request, *args, **kwargs):
    setting = Setting.objects.first()
    context = {
        "setting": setting,
    }
    return render(request, "shared/Header.html", context)

def footer_setting(request, *args, **kwargs):
    setting = Setting.objects.first()
    context = {
        "setting": setting,
    }
    return render(request, "shared/Footer.html", context)