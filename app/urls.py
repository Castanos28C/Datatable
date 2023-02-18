from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_programmers/', views.list_programmers, name='list_programmers'),
    path('programmer_edit/', views.programmer_edit, name='programmer_edit'),
    path('programmer_delete/<codigo>', views.programmer_delete, name='programmer_delete'),
    path('programmer_create/', views.programmer_create, name='programmer_create'),
    path('programmer/', views.programmer, name='programmer'),
]
