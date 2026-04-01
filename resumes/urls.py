from django.urls import path
from .views import ResumeUploadView

urlpatterns = [
    path("auth/resume/upload/", ResumeUploadView.as_view(), name="resume_upload"),
]
