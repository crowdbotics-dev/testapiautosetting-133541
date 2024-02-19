from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors133541ViewSet

router = DefaultRouter()
router.register(
    "testconnectors133541", Testconnectors133541ViewSet, basename="testconnectors133541"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
