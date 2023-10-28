from django.db import models
from django.contrib import admin

class FootballPlayer(models.Model):
    player_id = models.CharField(max_length=20, help_text="Player ID")
    p_name = models.CharField(max_length=100)
    p_team=models.CharField(max_length=100)
    captain_name=models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

class FootballPlayerAdmin(admin.ModelAdmin):
    list_display = ('player_id', 'p_name','p_team' ,'captain_name', 'age', 'email')


