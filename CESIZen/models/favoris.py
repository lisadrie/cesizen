from django.db import models
from django.utils import timezone
from .users import User
from .anecdotes import Anecdote

class FavoriteAnecdote(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    anecdote = models.ForeignKey(Anecdote, on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'anecdote') 

    def __str__(self):
        return f"{self.user.username} - {self.anecdote.get_type_display()}"
