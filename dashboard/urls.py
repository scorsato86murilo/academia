from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/ficha_treino_dash/', views.ficha_treino_dash, name='ficha_treino_dash'),
    path('dashboard/academia_dash/', views.academia_dash, name='academia_dash'),

    path('logout_view/', views.logout_view, name='logout_view'),
]
