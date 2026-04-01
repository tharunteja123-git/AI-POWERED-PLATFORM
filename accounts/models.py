from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES=(
        ('candidate', 'Candidate'),
        ('recruiter', 'Recruiter'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='candidate')
    skills = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    experience_years = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

