from django.contrib import admin
from actors.models import Actor


class ActorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nationality',)
