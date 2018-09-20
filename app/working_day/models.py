# -*- coding: utf-8 -*
from django.utils.translation import ugettext as _
from django.db import models


class WorkingDay(models.Model):
    """
    Working Day
    """

    name = models.CharField(
        'Name',
        max_length=128,
        blank=False,
        null=False,
        unique=True
    )

    code = models.CharField(
        'Code',
        max_length=8,
        blank=False,
        null=False
    )

    active = models.BooleanField(
        'Active',
        blank=True,
        null=False,
        default=True
    )

    class Meta:
        verbose_name = 'Working Day'
        verbose_name_plural = 'Working Days'

    def __str__(self):
        return self.name


DAY_OF_THE_WEEK = {
    '1': _(u'Monday'),
    '2': _(u'Tuesday'),
    '3': _(u'Wednesday'),
    '4': _(u'Thursday'),
    '5': _(u'Friday'),
    '6': _(u'Saturday'),
    '7': _(u'Sunday'),
}


class DayOfTheWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length'] = 1
        super(DayOfTheWeekField, self).__init__(*args, **kwargs)


class Schedule(models.Model):
    """
    Schedule
    """

    working_day = models.ForeignKey(
        WorkingDay,
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    dayOfTheWeek = DayOfTheWeekField()

    start = models.TimeField(
        'Start',
        null=False,
        blank=False
    )

    end = models.TimeField(
        'End',
        null=False,
        blank=False
    )

    active = models.BooleanField(
        'Active',
        blank=True,
        null=False,
        default=True
    )

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'

    def __str__(self):
        return '%s-%s' % (self.start, self.end)
