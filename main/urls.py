from django.urls import path
from . import views

urlpatterns = [
    path('commands/', views.CommandAPIView.as_view()),
]
