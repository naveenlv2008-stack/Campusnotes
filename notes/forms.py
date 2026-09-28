from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "subject", "semester", "unit", "description", "file"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Python Unit 2 Notes"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Python Programming"}),
            "semester": forms.Select(attrs={"class": "form-select"}),
            "unit": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Unit 2"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Short description"}),
            "file": forms.ClearableFileInput(attrs={"class": "form-control", "accept": ".pdf,.doc,.docx,.ppt,.pptx"}),
        }

    def clean_file(self):
        uploaded = self.cleaned_data["file"]
        allowed = [".pdf", ".doc", ".docx", ".ppt", ".pptx"]
        name = uploaded.name.lower()
        if not any(name.endswith(ext) for ext in allowed):
            raise forms.ValidationError("Only PDF, DOC, DOCX, PPT and PPTX files are allowed.")
        if uploaded.size > 50 * 1024 * 1024:
            raise forms.ValidationError("File size must be 10 MB or less.")
        return uploaded
