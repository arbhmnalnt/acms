from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Report
from .forms import ReportForm

class ReportListView(ListView):
    model = Report
    template_name = 'reports/report_list.html'

class ReportDetailView(DetailView):
    model = Report
    template_name = 'reports/report_detail.html'

class ReportCreateView(CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/report_form.html'
    success_url = reverse_lazy('reports:report_list')

class ReportUpdateView(UpdateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/report_form.html'
    success_url = reverse_lazy('reports:report_list')

class ReportDeleteView(DeleteView):
    model = Report
    template_name = 'reports/report_confirm_delete.html'
    success_url = reverse_lazy('reports:report_list')
