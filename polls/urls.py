from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [

        url('^$', views.index, name = 'index'),
        url('^(?P<question_id>[0-9]+)/$', views.detail, name = 'detail'),
        url('^(?P<question_id>[0-9]+)/$', views.results, name = 'results'),
        url('^(?P<question_id>[0-9]+)/$', views.results, name = 'vote'),

]
