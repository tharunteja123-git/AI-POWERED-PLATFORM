from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
import os
#import magic 

# file size
def validate_file_size(file):
    max_size = 10 * 1024 * 1024  
    if file.size > max_size:
        raise ValidationError("File size must be under 10 MB.")

# Custom validator for file extension
def validate_file_extension(file):
    valid_extensions = [".pdf", ".doc", ".docx"]
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError("Only PDF, DOC, and DOCX files are allowed.")


def validate_file_mime(file):
    valid_mimes = [
        "application/pdf",
        "application/msword",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ]
    '''mime = magic.from_buffer(file.read(1024), mime=True)
    file.seek(0)  
    if mime not in valid_mimes:
        raise ValidationError("Invalid file type. Only PDF/DOC/DOCX allowed.")'''

class Resume(models.Model):
    candidate = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='resumes'
    )
    file = models.FileField(
        upload_to='resumes/',
        blank=True,
        null=True,
        validators=[validate_file_size, validate_file_extension, validate_file_mime]
    )
    original_name = models.CharField(max_length=255, blank=True, null=True)
    mime_type = models.CharField(max_length=50, blank=True, null=True)
    text_content = models.TextField(blank=True, null=True) 
    parsed_skills = models.TextField(blank=True, null=True)
    experience_years = models.IntegerField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    contact_info = models.TextField(blank=True, null=True)
    is_parsed = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume of {self.candidate.username}"
