from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('rules', views.rules, name='rules'),
    path('contacts', views.contacts, name='contacts'),
    path('documents', views.documents, name='documents'),
    path('buy', views.buy, name='buy'),
    path('coop', views.coop, name='coop'),
    path('partner', views.partner, name='partner'),
]
