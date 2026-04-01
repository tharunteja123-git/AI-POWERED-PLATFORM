from django.db import models
from django.conf import settings

# Create your models here.
class Job(models.Model):
    recruiter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posted_jobs'
    )
    title=models.CharField(max_length=255)
    description=models.TextField()
    required_skills=models.TextField(help_text="Comma-separated list of skills")
    location=models.CharField(max_length=255)
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.recruiter.username})"
