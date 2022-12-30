from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'date', 'subject']


# Register your models here.
admin.site.register(Contact, ContactAdmin)