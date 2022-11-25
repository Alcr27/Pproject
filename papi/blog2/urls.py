from django.urls import path
from . import views
urlpatterns = [
    path('blog2/', views.muestra_datos, name='blog2'),
    path('knn/', views.muestra_datos, name='knn'),
    path('algoritmo1/', views.algKNN, name='algoritmo1'),
    path('algoritmoBaye/', views.algBaye, name='algoritmoBaye'),
    path('RALineal/', views.RLineal, name='RALineal'),
]
