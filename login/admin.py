from django.contrib import admin

<<<<<<< HEAD
# Register your models here.
=======
from login.models import Player, Team , Match ,AsignPoints,UserProfile


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

class PlayersInLine(admin.TabularInline):
    model = AsignPoints

class MatchAdmin(admin.ModelAdmin):
   fieldsets = [
       (None,       {'fields': ['match_name','pub_date','team_1','team_2']}),
   ]
   inlines = [PlayersInLine]

admin.site.register(Match, MatchAdmin)
admin.site.register(AsignPoints)
>>>>>>> 01f273e2d1c940e618083c134d88f8a90456d16f
