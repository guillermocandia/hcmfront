from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import WorkingDay
from .models import Schedule

from .serializers import WorkingDaySerializer
from .serializers import ScheduleSerializer
from .serializers import UserSerializer

from .filters import ScheduleFilter


class WorkingDayList(generics.ListCreateAPIView):
    queryset = WorkingDay.objects.all()
    serializer_class = WorkingDaySerializer


class WorkingDayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkingDay.objects.all()
    serializer_class = WorkingDaySerializer


class ScheduleList(generics.ListCreateAPIView):
    filter_class = ScheduleFilter
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class CheckToken(APIView):
    serializer_class = UserSerializer

    def get(self, request, format=None):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data)
