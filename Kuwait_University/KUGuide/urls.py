from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('faq/', views.faq, name='faq'),
    path('career/', views.career, name='career'),
    path('contact/', views.contact, name='contact'),
]