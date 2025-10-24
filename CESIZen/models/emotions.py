from django.db import models
from django.utils import timezone
from .users import User

class Emotion(models.Model):
    class EmotionType(models.TextChoices):
        TRISTE = 'TR', 'Triste'
        ANGOISSE = 'AN', 'Angoissé'
        AMOUREUX = 'AM', 'Amoureux'
        HEUREUX = 'HE', 'Heureux'
        CALME = 'CA', 'Calme'
        STRESSE = 'ST', 'Stressé'
        FATIGUE = 'FA', 'Fatigué'
        APAISE = 'AP', 'Apaisé'
        CONFIANT = 'CO', 'Confiant'
        INCOMPRIS = 'IC', 'Incompris'
        SEUL = 'SE', 'Seul'
        TEMPETE = 'TE', 'En tempête émotionnelle'

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emotions')
    emotion = models.CharField(max_length=2, choices=EmotionType.choices)
    intensity = models.PositiveSmallIntegerField(default=1)  
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.get_emotion_display()} ({self.intensity})"
