from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee
from .forms import EmployeeForm

class EmployeeListView(ListView):
    model = Employee
    template_name = 'hr/employee_list.html'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'hr/employee_detail.html'

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'hr/employee_form.html'
    success_url = reverse_lazy('hr:employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'hr/employee_form.html'
    success_url = reverse_lazy('hr:employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'hr/employee_confirm_delete.html'
    success_url = reverse_lazy('hr:employee_list')
