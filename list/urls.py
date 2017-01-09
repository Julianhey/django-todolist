from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^todo/(?P<pk>\d+)/$', views.todo_detail, name='todo_detail'),
    url(r'^todo/new/$', views.todo_new, name='todo_new'),
    url(r'^todo/(?P<pk>\d+)/edit/$', views.todo_edit, name='todo_edit'),
    url(r'^todo/(?P<pk>\d+)/remove/$', views.todo_remove, name='todo_remove'),
    url(r'^todo/(?P<pk>\d+)/comment/$', views.add_comment_to_todo, name='add_comment_to_todo'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^mylibrary/$', views.GameLibraryView.as_view(), name='my-library'),
    url(r'^mylibrary/add/$', views.game_add, name='game_add'),
]
