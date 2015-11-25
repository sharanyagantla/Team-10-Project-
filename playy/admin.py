from django.contrib import admin

from .models import Player, Team , Match

admin.site.register(Player)

class PlayerInLine(admin.TabularInline):
    model = Player
    extra = 3

class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,       {'fields': ['team_name']}),
    ]
    inlines = [PlayerInLine]
    search_fields = ['team_name']


class MatchAdmin(admin.ModelAdmin):
   fieldsets = [
       (None,       {'fields': ['match_name','pub_date','team_1' , 'team_2']}),
   ]


admin.site.register(Match, MatchAdmin)

admin.site.register(Team, TeamAdmin)

