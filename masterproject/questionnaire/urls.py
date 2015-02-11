from django.conf.urls import patterns, url

from questionnaire import views

urlpatterns = patterns('',
    url(r'^rules', views.rules, name='rules'),
    url(r'^training', views.training, name='training'),
    url(r'^patterninformation', views.patterninformation, name='patterninformation'),
    url(r'^pattern1', views.pattern1, name='pattern1'),
    url(r'^pattern2', views.pattern2, name='pattern2'),
    url(r'^pattern3', views.pattern3, name='pattern3'),
    url(r'^add_handsize', views.add_handsize, name='add_handsize'),
    url(r'^nomobile', views.nomobile, name='nomobile'),
    url(r'^add_screensize', views.add_screensize, name='add_screensize'),
    url(r'^add_handedness', views.add_handedness, name='add_handedness'),
    url(r'^add_finger', views.add_finger, name='add_finger'),
    url(r'^add_reading', views.add_reading, name='add_reading'),
    url(r'^add_gender', views.add_gender, name="add_gender"),
    url(r'^add_age', views.add_age, name='add_age'),
    url(r'^add_nationality', views.add_nationality, name='add_nationality'),
    url(r'^add_usedALP', views.add_usedALP, name='add_usedALP'),
    url(r'^add_useScreenlock', views.add_useScreenlock, name='add_useScreenlock'),
    url(r'^add_screenlock', views.add_screenlock, name='add_screenlock'),
    url(r'^add_mobileOS', views.add_mobileOS, name='add_mobileOS'),
    url(r'^add_experience', views.add_experience, name='add_experience'),
    url(r'^finish', views.finish, name='finish'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^$', views.index, name='index'),
)
