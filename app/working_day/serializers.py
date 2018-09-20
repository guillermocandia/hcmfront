from django.contrib.auth.models import User
from rest_framework import serializers

from .models import WorkingDay
from .models import Schedule


class WorkingDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingDay
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_login', 'is_superuser',
                  'first_name', 'last_name', 'email',
                  'is_staff', 'is_active', 'date_joined')
