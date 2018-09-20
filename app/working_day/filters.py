from django_filters.rest_framework import FilterSet

from .models import Schedule


class ScheduleFilter(FilterSet):
    class Meta:
        model = Schedule
        fields = {
            'working_day': ['exact']
        }
