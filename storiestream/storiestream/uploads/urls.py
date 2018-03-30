from django.urls import path, include
from . import views

app_name = 'uploads'
urlpatterns = [
    path('storiestream/storiestream/uploads', views.index, name='uploads')
]
