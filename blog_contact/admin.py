from django.contrib import admin

# Register your models here.
from blog_contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    search_fields = ['name', 'content']


admin.site.register(Contact, ContactAdmin)
