from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index),
    path('get/', views.GetAllPost),
    path('create-post/', views.CreatePost),
    path('delete-post/<int:id>/', views.DeletePost),
    path('get-post/<int:id>/', views.GetSingle),
     path('update-post/<int:id>/', views.UpdatePost),
]