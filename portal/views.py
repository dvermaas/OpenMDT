from django.shortcuts import render
from django.http import HttpResponse
from .models import Report


def index(request):
    latest_report_list = Report.objects.order_by("-created_at")[:5]
    context = {"latest_report_list": latest_report_list}
    return render(request, "portal/index.html", context)


def detail(request, report_id):
    report = Report.objects.get(id=report_id)
    context = {"report": report}
    return render(request, "portal/detail.html", context)
