from django.contrib import admin
from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'stars')


admin.site.register(Review, ReviewAdmin)
