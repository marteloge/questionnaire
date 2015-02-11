from django.conf.urls import patterns, include, url
from django.contrib import admin

handler404 = 'questionnaire.views.custom_404'
handler500 = 'questionnaire.views.custom_500'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('questionnaire.urls', namespace="questionnaire")),
)