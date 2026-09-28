from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "semester", "uploaded_by", "downloads", "created_at")
    search_fields = ("title", "subject", "description")
    list_filter = ("semester", "created_at")
