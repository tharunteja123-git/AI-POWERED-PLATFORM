from django.db import models
from django.conf import settings
from jobs.models import Job
from resumes.models import Resume
from resumes.utils import calculate_match_score


# Create your models here.
class Application(models.Model):
    candidate=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    job=models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='applications'

    )

    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name='applications',
        null=True, blank=True
     )
    STATUS_CHOICES=(
        ('applied', 'Applied'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    applied_at = models.DateTimeField(auto_now_add=True)
    match_score = models.FloatField(blank=True, null=True)

    def save(self,*args,**kwargs):
        if self.resume and self.job:
            self.match_score=calculate_match_score(self.resume.text_content,self.job.description)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.candidate.username} → {self.job.title} ({self.status})"