from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="home"),
    path("insert/", views.insert, name="insert"),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('result/', views.result, name='result'),
    path('edit/', views.edit, name='edit'),
    path('deletes/', views.deletes, name='deletes'),
    path('save/<int:num>', views.save, name='save'),
    path("introduce/", views.introduce, name="introduce"),
    path("test/", views.test, name="test"),
    path("details/<int:num>", views.details, name="details"),




]