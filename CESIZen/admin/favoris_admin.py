from django.contrib import admin
from ..models.favoris import FavoriteAnecdote

@admin.register(FavoriteAnecdote)
class FavoriteAnecdoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'anecdote', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'anecdote__content')
    ordering = ('-created_at',)
