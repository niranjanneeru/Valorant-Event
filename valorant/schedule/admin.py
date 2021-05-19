from django.contrib import admin

from .models import Team, Final, QuarterFinal, SemiFinal, KnockOut


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Final)
class FinalAdmin(admin.ModelAdmin):
    list_display = ['team1', 'team2', 'winner', 'date']


@admin.register(QuarterFinal)
class QFAdmin(admin.ModelAdmin):
    list_display = ['team1', 'team2', 'winner', 'date']


@admin.register(SemiFinal)
class SFAdmin(admin.ModelAdmin):
    list_display = ['team1', 'team2', 'winner', 'date']


@admin.register(KnockOut)
class KOAdmin(admin.ModelAdmin):
    list_display = ['team1', 'team2', 'winner', 'date']
