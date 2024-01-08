from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import HabitViewSet, UserViewSet, ProgressViewSet

router = DefaultRouter(trailing_slash='')
router.register(r'habits', HabitViewSet)
router.register(r'users', UserViewSet)
router.register(r'progress', ProgressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
