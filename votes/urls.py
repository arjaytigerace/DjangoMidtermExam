from django.urls import path
from django.contrib import admin
from django.urls import path
from .import views
app_name ="votes"

urlpatterns = [
    path('', views.index, name="index"),
    #path('create/', views.create, name="create")
]
