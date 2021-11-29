from django.urls import path

from . import views #. is this folder

app_name = 'MainApp'

urlpatterns = [
    path('',views.index, name='index'),
    path('topics',views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
]