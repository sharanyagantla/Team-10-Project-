from django.contrib import admin

from .models import Player, Team , Match ,AsignPoints , UserProfile , Points

admin.site.register(Player)
admin.site.register(UserProfile)

class PlayerInLine(admin.TabularInline):
    model = Player
    extra = 3

class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,       {'fields': ['team_name']}),
    ]
    inlines = [PlayerInLine]
    search_fields = ['team_name']

admin.site.register(Team, TeamAdmin)

class AsignPointsInLine(admin.TabularInline):
    model = AsignPoints
    extra = 11

class MatchAdmin(admin.ModelAdmin):
   fieldsets = [
       (None,       {'fields': ['match_name','pub_date','team_1','team_2']}),
   ]
   inlines = [AsignPointsInLine]

admin.site.register(Match, MatchAdmin)
admin.site.register(AsignPoints)
admin.site.register(Points)







