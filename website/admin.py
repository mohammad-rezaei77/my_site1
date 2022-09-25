from tabnanny import verbose
from django.contrib import admin
from website.models import contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'update_date')
    list_filter = ('create_date',)
    search_fields = ('subject','message')

admin.site.register(contact,ContactAdmin)
