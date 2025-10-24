# CESIZen/models.py
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.email
