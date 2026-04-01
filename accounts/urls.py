from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, CustomTokenObtainPairView
from resumes.views import ResumeUploadView


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(serializer_class=CustomTokenObtainPairSerializer)),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/resume/upload/", ResumeUploadView.as_view(), name="resume_upload"),

    
]
