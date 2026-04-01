from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsCandidate
from .models import Application
from .serializers import ApplicationSerializer

# Create your views here.

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]


    def get_permissions(self):
        if self.action == 'create':
            return [IsCandidate()]
        return [IsAuthenticated()]


