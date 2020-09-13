from django.shortcuts import render

# Create your views here.
from blog_about.models import AboutMe


def about_page(request):
    about = AboutMe.objects.first()
    context = {
        "about": about
    }
    return render(request, 'about.html', context)
