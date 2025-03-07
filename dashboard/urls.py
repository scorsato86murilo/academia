from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/ficha_treino_dash/', views.ficha_treino_dash, name='ficha_treino_dash'),
    path('dashboard/academia_dash/', views.academia_dash, name='academia_dash'),
    path('dashboard/mensalidades/', views.mensalidades, name='mensalidades'),
    path('dashboard/nossos_produtos/', views.nossos_produtos, name='nossos_produtos'),
    path('dashboard/editar_produtos/id/<int:pk>', views.editar_produtos, name='editar_produtos'),
    path('produto/excluir/<int:pk>/', views.excluir_produto, name='excluir_produto'),
    path('deleta_obj_academia/<int:id>/', views.deleta_obj_academia, name='deleta_obj_academia'),
    path('dashboard/personal', views.personal, name='personal'),
    path('personal/<int:pk>/editar/', views.atualizar_personal, name='atualizar_personal'),
    path('personal/excluir/<int:pk>/', views.excluir_personal, name='excluir_personal'),
    path('logout_view/', views.logout_view, name='logout_view'),
]
