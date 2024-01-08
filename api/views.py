from django.http import Http404
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response

from api.models import Habit, CustomUser, Progress
from api.serializers import UserSerializer, HabitSerializer, ProgressSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    @action(detail=False, methods=['get'], url_path="get_active_habits_sorted")
    def get_active_habits_sorted(self):
        habit = Habit.objects.filter(is_active=True).order_by('start_date')
        serializer = self.get_serializer(habit, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='mark_completed')
    def mark_completed(self, habit_id=None):
        try:
            habit = self.get_queryset().get(id=habit_id)
            habit.is_completed = True
            habit.save()
            serializer = self.get_serializer(habit)
            return Response(serializer.data)
        except Http404:
            return Response({"error": "Habbit not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'], url_path='mark_done')
    def mark_done(self, request):
        print("HERE!")

        habit_id = self.request.query_params.get('habit_id')
        habit = self.get_queryset().get(id=habit_id)
        habit.is_done_today = True
        habit.save()
        serializer = self.get_serializer(habit)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class ProgressViewSet(viewsets.ModelViewSet):
    serializer_class = ProgressSerializer
    queryset = Progress.objects.all()
