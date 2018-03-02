from django.conf.urls import url
from . import views


app_name = 'discussions'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<topic_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^new/$', views.new, name='new'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<topic_id>[0-9]+)/comment/$', views.comment, name='comment'),
]
