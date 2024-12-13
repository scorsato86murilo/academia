from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/ficha_treino_dash/', views.ficha_treino_dash, name='ficha_treino_dash'),
]
