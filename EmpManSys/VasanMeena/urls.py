

from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.dispHome),
    path('adminFeat/',  views.adminFeat),
    path('empFeat/', views.empFeat),
    path('showEmps/<str:id>/<str:secnum>/', views.showEmps),
    path('createEntry/<str:id>/<str:secnum>/', views.createEntry),
    path('update/<str:eid>/<str:id>/<str:secnum>/', views.update),
    path('delete/<str:eid>/<str:id>/<str:secnum>/', views.delete),
    ]
