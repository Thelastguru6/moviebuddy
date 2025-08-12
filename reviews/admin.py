from django.contrib import admin
from .models import Movie, Review

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'created_at')
    search_fields = ('title',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('movie__title', 'user__username', 'title', 'body')

admin.site.site_header = "MovieBuddy Admin"
admin.site.site_title = "MovieBuddy Admin Portal"
admin.site.index_title = "Welcome to the MovieBuddy Admin Portal"