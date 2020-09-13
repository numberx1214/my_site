from django.urls import path

from blog_about.views import about_page

urlpatterns = [
    path("about", about_page, name="about")
]
