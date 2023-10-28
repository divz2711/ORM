from django.contrib import admin
from .models import FootballPlayer,FootballPlayerAdmin
admin.site.register(FootballPlayer,FootballPlayerAdmin)