from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(product)
@admin.register(models.Register)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile','gender']