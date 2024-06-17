from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView

from .models import Report, Suspect
from profiles.models import Profile
from .forms import ReportForm, ReportSuspectForm


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    # fields = ["title", "is_warrant", "is_processed", "is_plead_guilty"]
    form_class = ReportForm
    template_name = "reports/create.html"
    success_url = "/reports"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


def add_suspect_to_report(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    if request.method == "POST":
        Suspect.objects.create(profile=Profile.objects.last(), report=report)
        return redirect("detail", report_id=report.id)
    context = {"report": report}
    return render(request, "reports/detail.html", context)


def index(request):
    latest_report_list = Report.objects.order_by("-created_at")[:]
    context = {"latest_report_list": latest_report_list}
    return render(request, "reports/index.html", context)


def detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    context = {"report": report}
    return render(request, "reports/detail.html", context)


def edit(request, pk):
    report = get_object_or_404(Report, pk=pk)
    context = {"report": report}
    return render(request, "reports/index.html", context)


def delete(request, pk):
    report = get_object_or_404(Report, pk=pk)
    report.delete()
    return index(request)
