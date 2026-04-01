"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from jobs.views import JobViewSet
from accounts.views import UserViewSet
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
from resumes.views import ResumeViewSet


router=routers.DefaultRouter()
router.register(r'jobs',JobViewSet)
router.register(r'users', UserViewSet)
router.register(r'resumes', ResumeViewSet)


urlpatterns = [
    #path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path("api/", include("accounts.urls")),
    path("", include("resumes.urls")),
    path("", include("jobs.urls")),

]

# urls.py
# from django.urls import path
# from jobs.views import register, login

# urlpatterns = [
#     path('auth/register/', register),
#     path('auth/login/', login),
# ]
