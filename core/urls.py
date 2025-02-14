from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('<int:id>/', views.patient_detail, name='patient_detail'),
]