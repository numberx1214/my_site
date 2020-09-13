from django.urls import path

from .views import header_setting, footer_setting

urlpatterns = [
    path("header", header_setting, name="header"),
    path("footer", footer_setting, name="footer")
]
