# -*- coding: utf-8 -*
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view
# from django.conf import settings
# from django.conf.urls.static import static


schema_view = get_swagger_view(title='Jornadas API')

admin.site.site_header = 'Jornadas Administración'

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^index.html$', schema_view),
    # url(r'^auth/user/', AuthUser.as_view()),
    url(r'^auth/', views.obtain_auth_token),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
]
