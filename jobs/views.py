from django.shortcuts import render
from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsRecruiter
from rest_framework import generics, permissions
# Create your views here.
class JobViewSet(viewsets.ModelViewSet):
    queryset=Job.objects.all()
    serializer_class=JobSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsRecruiter()]
        return [IsAuthenticated()]
class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all().order_by("-posted_at")
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)
