from django.urls import path
from . import views

urlpatterns = [
    path('terminal/', views.terminal_view, name='terminal'),
    path('/api/', views.terminal_api, name='terminal_api'),
]
