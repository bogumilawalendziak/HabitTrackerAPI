from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import HabitViewSet, UserViewSet

router = DefaultRouter()
router.register(r'habits', HabitViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
