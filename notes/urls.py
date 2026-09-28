from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("upload/", views.upload_note, name="upload_note"),
    path("my-notes/", views.my_notes, name="my_notes"),
    path("bookmarks/", views.bookmarks, name="bookmarks"),
    path("bookmark/<int:note_id>/", views.bookmark, name="bookmark"),
    path("download/<int:note_id>/", views.download_note, name="download_note"),
]
