from django.contrib import admin
from .models import users, teams

admin.site.register(users)
admin.site.register(teams)