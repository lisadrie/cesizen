from django.contrib import admin
from ..models.emotions import Emotion

@admin.register(Emotion)
class EmotionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'emotion', 'intensity', 'created_at')
    list_filter = ('emotion', 'intensity', 'created_at')
    search_fields = ('user__pseudo',)
    ordering = ('-created_at',)
