from django.urls import path

from blog_contact.views import contact

urlpatterns = [
    path('contact', contact, name="contact"),
]
