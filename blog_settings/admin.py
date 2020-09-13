from django.contrib import admin

# Register your models here.
from blog_settings.models import Setting

admin.site.register(Setting)