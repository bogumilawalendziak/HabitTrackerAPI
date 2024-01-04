from django.http import Http404
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response

from api.models import Habit, CustomUser
from api.serializers import UserSerializer, HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    @action(detail=False, methods=['get'])
    def get_active_habits_sorted(self):
        habit = Habit.objects.filter(is_active=True).order_by('start_date')
        serializer = self.get_serializer(habit, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def mark_completed(self, request):
        try:
            habit_id = request.data.get('habit_id')
            habit = self.get_queryset().get(id=habit_id)
            habit.is_completed = True
            habit.save()
            serializer = self.get_serializer(habit)
            return Response(serializer.data)
        except Http404:
            return Response({"error": "Habbit not found"}, status=status.HTTP_404_NOT_FOUND)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
