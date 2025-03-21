from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('labs/', views.labs, name='digital-labs')
]
