from django.urls import path
from . import views


urlpatterns = [

    path('contato/grupoContatos', views.grupoContatos, name="grupoContatos"),
    path('contato/grupoContatos/add',
         views.grupoContatos_add, name="grupoContatos_add"),
    path('contato/grupoContatos/edit/<int:grupoContatos_pk>',
         views.grupoContatos_edit, name="grupoContatos_edit"),
    path('contato/grupoContatos/delete/<int:grupoContatos_pk>',
         views.grupoContatos_delete, name="grupoContatos_delete"),

    path('contato/', views.contato, name="contato"),
    path('contato/add/', views.contato_add, name="contato_add"),
    path('contato/edit/<int:contato_pk>',
         views.contato_edit, name="contato_edit"),
    path('contato/delete/<int:contato_pk>',
         views.contato_delete, name="contato_delete"),
]
