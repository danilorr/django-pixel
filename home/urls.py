from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/rent-calculator/', views.rent_calculator, name='rent-calculator')
]
