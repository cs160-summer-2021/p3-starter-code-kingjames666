from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.index, name='new_interaction'),
    path('frame1', views.frame1, name='frame1'),
    path('frame2', views.frame2, name='frame2')
]
