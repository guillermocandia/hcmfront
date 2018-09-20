from django.contrib import admin

from .models import WorkingDay
from .models import Schedule


class ScheduleInline(admin.TabularInline):
    model = Schedule


class WorkingDayAdmin(admin.ModelAdmin):
    inlines = [
        ScheduleInline
    ]


admin.site.register(WorkingDay, WorkingDayAdmin)
admin.site.register(Schedule)
