from django.urls import path

from . import views #. is this folder

app_name = 'MainApp'

urlpatterns = [
    path('',views.index, name='index'),
]