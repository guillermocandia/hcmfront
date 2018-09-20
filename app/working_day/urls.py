from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^working-day/$',
        views.WorkingDayList.as_view(),
        name='working-day-list'),
    url(r'^working-day/(?P<pk>[0-9]+)/$',
        views.WorkingDayDetail.as_view(),
        name='working-day-detail'),
    url(r'^schedule/$',
        views.ScheduleList.as_view(),
        name='schedule-list'),
    url(r'^schedule/(?P<pk>[0-9]+)/$',
        views.ScheduleDetail.as_view(),
        name='schedule-detail'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
