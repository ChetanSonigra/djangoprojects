from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('complete/<str:pk>', views.complete, name = 'complete'),
    path('sort/<str:pk>', views.sort, name = 'sort' )
]
