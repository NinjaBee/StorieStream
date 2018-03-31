from django.urls import path, include
from . import views

app_name = 'editing'
urlpatterns = [
    path('storiestream/storiestream/editing', views.index, name='editing')
]

