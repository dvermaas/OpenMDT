from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import QueryDict
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView

from profiles.models import Profile
from reports.forms import ReportForm, ReportCrispyForm
from reports.models import Report, Suspect


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
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
    reports = Report.objects.filter(is_active=True).order_by("-created_at")
    context = {"latest_report_list": reports}
    return render(request, "reports/index.html", context)


def table(request):
    reports = Report.objects.filter(is_active=True).order_by("-created_at")
    paginator = Paginator(reports, 25)
    page = paginator.get_page(request.GET.get("page"))
    context = {"reports": page}
    return render(request, "reports/partials/table.html", context)


def detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    context = {"report": report}
    return render(request, "reports/detail.html", context)


def detail_info_form(request, pk):
    report = get_object_or_404(Report, pk=pk)
    context = {"report": report}
    if request.method == "PUT":
        data = QueryDict(request.body)
        form = ReportForm(data, instance=report)
        if form.is_valid():
            form.save()
            return render(request, "reports/partials/info.html", context)
    context["form"] = ReportForm(instance=report)
    return render(request, "reports/partials/info-form.html", context)


def delete(request, pk):
    report = get_object_or_404(Report, pk=pk)
    report.is_active = False
    report.save()
    return index(request)


def form(request):
    context = {"form": ReportCrispyForm()}
    if request.method == "POST":
        print("posting")
        form = ReportCrispyForm(request.POST)
        if form.is_valid():
            # form.save()
            return redirect("reports:index")
    return render(request, "reports/create.html", context)
