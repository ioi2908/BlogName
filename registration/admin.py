from django.contrib import admin
from registration.models import Register, Profile


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['first_name',
                    'last_name']


admin.site.register(Register, RegisterAdmin),
admin.site.register(Profile)

from django.contrib.admin import AdminSite



class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'

admin_site = MyAdminSite(name='admin')
