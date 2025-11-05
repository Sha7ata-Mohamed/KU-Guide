from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('faq/', views.faq, name='faq'),
    path('career/', views.career, name='career'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('signin/', views.signin, name='signin'),
]