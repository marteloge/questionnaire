from django.conf.urls import patterns, url

from questionnaire import views

urlpatterns = patterns('',
   	url(r'^$', views.index, name='index'),
    url(r'^view1', views.view1, name='view1'),
    url(r'^view2', views.view2, name='view2'),
    url(r'^add_gender', views.add_gender, name="add_gender"),
)