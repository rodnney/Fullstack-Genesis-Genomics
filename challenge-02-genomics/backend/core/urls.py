"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from genes.views import GeneViewSet

router = DefaultRouter()
router.register(r'genes', GeneViewSet, basename='gene')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
