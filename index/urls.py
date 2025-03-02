from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ficha_treino/', views.ficha_treino, name='ficha_treino'),
    path('login_/', views.login_, name='login_'),
    path('cadastro_login_/', views.cadastro_login_, name='cadastro_login_'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('academia/', views.academia, name='academia'),
    path('produto/vendas/', views.produto_vendas, name='produto_vendas'),
    path('personal/', views.personal, name='personal_index'),

]