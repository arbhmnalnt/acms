from django.urls import path
from .views import (
    EmployeeListView,
    EmployeeDetailView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
)

app_name = 'hr'
urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/add/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
]
