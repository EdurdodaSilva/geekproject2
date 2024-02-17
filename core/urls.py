from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('produto/<int:id>/', views.produto, name='produto'),
]
