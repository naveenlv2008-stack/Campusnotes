from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note

def home(request):
    query = request.GET.get("q", "").strip()
    semester = request.GET.get("semester", "").strip()

    notes = Note.objects.all()

    if query:
        notes = notes.filter(
            Q(title__icontains=query)
            | Q(subject__icontains=query)
            | Q(description__icontains=query)
        )

    if semester:
        notes = notes.filter(semester=semester)

    return render(request, "home.html", {
        "notes": notes,
        "query": query,
        "semester": semester,
        "semesters": range(1, 9),
    })

def signup(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})

@login_required
def upload_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.uploaded_by = request.user
            note.save()
            messages.success(request, "Your note was uploaded successfully!")
            return redirect("home")
    else:
        form = NoteForm()

    return render(request, "upload.html", {"form": form})

@login_required
def my_notes(request):
    notes = Note.objects.filter(uploaded_by=request.user)
    return render(request, "my_notes.html", {"notes": notes})

@login_required
def bookmark(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if note.bookmarked_by.filter(id=request.user.id).exists():
        note.bookmarked_by.remove(request.user)
        messages.info(request, "Removed from bookmarks.")
    else:
        note.bookmarked_by.add(request.user)
        messages.success(request, "Added to bookmarks.")
    return redirect(request.META.get("HTTP_REFERER", "home"))

@login_required
def bookmarks(request):
    notes = request.user.bookmarked_notes.all()
    return render(request, "bookmarks.html", {"notes": notes})

def download_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if not note.file:
        raise Http404("File not found.")
    note.downloads += 1
    note.save(update_fields=["downloads"])
    try:
        return FileResponse(
            note.file.open("rb"),
            as_attachment=True,
            filename=note.file.name.split("/")[-1],
        )
    except FileNotFoundError:
        raise Http404("File not found.")
