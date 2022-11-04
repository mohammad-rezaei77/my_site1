import email
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *
from .models import User
from django.contrib.auth.models import Group

# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = UserchangeForm
    add_form = UserCreateForm
    list_display = ('email','username','phone')
    list_filter = ('email' , 'is_active')
    fieldsets = (
        ('User' ,{'fields':('email','password')}) ,
        ('Personal information',{'fields':('is_admin',)}),
        ('Permission' ,{'fields':('is_active',)})

    )
    add_fieldsets = (
        (None,{'fields':('email', 'username', 'name', 'phone', 'password1', 'password2' ,)}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User,UserAdmin)
admin.site.unregister(Group)
