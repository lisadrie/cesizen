from django.db import models
from django.utils import timezone

class Anecdote(models.Model):

    class AnecdoteType(models.TextChoices):
        FUNFACTS = 'FU', 'Fun facts'
        RASSURANTE = 'RA', 'Rassurante'

    id = models.AutoField(primary_key=True)
    type = models.CharField(
        max_length=2,
        choices=AnecdoteType.choices,
        default=AnecdoteType.FUNFACTS
    )
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.get_type_display()} - {self.content[:30]}..."
