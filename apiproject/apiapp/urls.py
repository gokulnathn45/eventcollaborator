from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users',UserViewSet)


class EventViewSet:
    pass


router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]