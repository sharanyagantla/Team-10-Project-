from django.contrib import admin
from .models import Player, Team , Match ,AsignPoints

class PlayerInLine(admin.TabularInline):
    model = Player
    extra = 3

class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,       {'fields': ['team_name']}),
    ]
    inlines = [PlayerInLine]
    search_fields = ['team_name']

class PlayersInLine(admin.TabularInline):
    model = AsignPoints

class MatchAdmin(admin.ModelAdmin):
   fieldsets = [
       (None,       {'fields': ['match_name','pub_date','team_1','team_2']}),
   ]
   inlines = [PlayersInLine]

admin.site.register(Player)

admin.site.register(Team, TeamAdmin)

admin.site.register(Match, MatchAdmin)
admin.site.register(AsignPoints)
