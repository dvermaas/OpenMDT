from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
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
    return render(request, "reports/index.html")


def table(request):
    page = request.GET.get("page", 1)
    cache_key = f"reports/table/page={page}"
    cached_page = cache.get(cache_key)
    if cached_page:
        return cached_page

    reports = Report.objects.filter(is_active=True).order_by("-created_at")
    page = Paginator(reports, 15).get_page(request.GET.get("page", 1))
    rendered_page = render(request, "reports/partials/table.html", {"reports": page})
    cache.set(cache_key, rendered_page, 60 * 5)
    return rendered_page


def detail(request, pk):
    print("Cache miss:", pk)
    report = get_object_or_404(Report, pk=pk)
    response = render(request, "reports/detail.html", {"report": report})
    return response


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
