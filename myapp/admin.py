from django.contrib import admin
from . import models

# Register your models here.

# admin.site.register(User)

#admin.site.register(User)

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile']
