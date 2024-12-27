from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ficha_treino/', views.ficha_treino, name='ficha_treino'),
    path('login_/', views.login_, name='login_')

]