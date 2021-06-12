from django.contrib import admin
from .models import Profile

admin.site.site_header = 'Admin page'
admin.site.register(Profile)
