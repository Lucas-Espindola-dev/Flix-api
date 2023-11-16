from django.contrib import admin
from genres.models import Genre


class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


admin.site.register(Genre, GenresAdmin)
