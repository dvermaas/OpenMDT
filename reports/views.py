from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView

from .models import Report
from .forms import YourModelForm


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    # fields = ["title"]
    form_class = YourModelForm
    template_name = "reports/create.html"
    success_url = "/reports"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


def index(request):
    latest_report_list = Report.objects.order_by("-created_at")[:]
    context = {"latest_report_list": latest_report_list}
    return render(request, "reports/index.html", context)


def detail(request, report_id):
    report = Report.objects.get(id=report_id)
    context = {"report": report}
    return render(request, "reports/detail.html", context)


def edit(request, report_id):
    report = Report.objects.get(id=report_id)
    context = {"report": report}
    return render(request, "reports/index.html", context)


def delete(request, report_id):
    report = Report.objects.get(id=report_id)
    report.delete()
    return render(request, "reports/index.html")
