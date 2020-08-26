from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('username','email','first_name','is_staff','is_active')
    list_filter = ('date_joined','last_login')
    fieldsets = (
        ( 'Active', {'fields': ('is_active',)}
     ),
        )
admin.site.unregister(User)
admin.site.register(User, UserAdmin)