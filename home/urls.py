from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('curiosidades/', views.curiosidades, name='curiosidades'),
    path('contato/', views.contato, name='contato'),
]