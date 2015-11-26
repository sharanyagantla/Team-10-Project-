from django.contrib import admin
<<<<<<< HEAD

from .models import Player, Team , Match ,AsignPoints



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

admin.site.register(Team, TeamAdmin)

class PlayersInLine(admin.TabularInline):
    model = AsignPoints

class MatchAdmin(admin.ModelAdmin):
   fieldsets = [
       (None,       {'fields': ['match_name','pub_date','team_1','team_2']}),
   ]
   inlines = [PlayersInLine]

admin.site.register(Match, MatchAdmin)








<<<<<<< HEAD
from .models import Player, Team , Match ,AsignPoints



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






=======
# Register your models here.
=======
>>>>>>> 63db62f4c73dc5f00ed00e4a89f79f9634d8944c
>>>>>>> d1c94c9d04de9168cc110551037b0345be010529
