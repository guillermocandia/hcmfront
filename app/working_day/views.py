from rest_framework import generics

from .models import WorkingDay
from .models import Schedule

from .serializers import WorkingDaySerializer
from .serializers import ScheduleSerializer

from .filters import ScheduleFilter


class WorkingDayList(generics.ListCreateAPIView):
    queryset = WorkingDay.objects.all()
    serializer_class = WorkingDaySerializer


class WorkingDayDetail(generics.RetrieveAPIView):
    queryset = WorkingDay.objects.all()
    serializer_class = WorkingDaySerializer


class ScheduleList(generics.ListCreateAPIView):
    filter_class = ScheduleFilter
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleDetail(generics.RetrieveAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
