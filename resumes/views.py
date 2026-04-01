from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Resume
from .serializers import ResumeSerializer
from .utils import extract_skills, calculate_match_score
from jobs.models import Job
from rest_framework import generics, permissions


# Create your views here.

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    @action(detail=True, methods=['post'])
    def match_job(self, request, pk=None):
        resume = self.get_object()
        job_id = request.data.get('job_id')
        job = Job.objects.get(id=job_id)

        score = calculate_match_score(resume.text_content, job.description)
        skills = extract_skills(resume.text_content)

        return Response({
            "resume_id": resume.id,
            "job_id": job.id,
            "match_score": score,
            "extracted_skills": skills
        })
class ResumeUploadView(generics.CreateAPIView):
        queryset = Resume.objects.all()
        serializer_class = ResumeSerializer
        permission_classes = [permissions.IsAuthenticated]

def perform_create(self, serializer):
        serializer.save(user=self.request.user)


