from django.contrib import admin
from ..models.users import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "created_at")
    search_fields = ("email", "username",)
