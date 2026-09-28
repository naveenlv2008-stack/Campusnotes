from django.contrib.auth.models import User
from django.db import models

class Note(models.Model):
    SEMESTER_CHOICES = [(str(i), f"Semester {i}") for i in range(1, 9)]

    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES)
    unit = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="notes/")
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    created_at = models.DateTimeField(auto_now_add=True)
    downloads = models.PositiveIntegerField(default=0)
    bookmarked_by = models.ManyToManyField(User, related_name="bookmarked_notes", blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
