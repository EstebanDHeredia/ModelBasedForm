from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'contact_type', 'created_at', 'subscription')
    search_fields = ('name', 'email', 'message')
    list_filter = ('name', 'email', 'contact_type')


admin.site.register(Contact, ContactAdmin)