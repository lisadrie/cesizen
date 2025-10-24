from django.contrib import admin
from CESIZen.models.anecdotes import Anecdote

@admin.register(Anecdote)
class AnecdoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'content', 'created_at')
    list_filter = ('type', 'created_at')
    search_fields = ('content',)
    ordering = ('-created_at',)
