from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Report
from .forms import YourModelForm


def index(request):
    latest_report_list = Report.objects.order_by("-created_at")[:5]
    context = {"latest_report_list": latest_report_list}
    return render(request, "reports/index.html", context)


def detail(request, report_id):
    report = Report.objects.get(id=report_id)
    context = {"reports": report}
    return render(request, "reports/detail.html", context)


# def add(request, report_id):
#     reports = Report.objects.get(id=report_id)
#     context = {"reports": reports}
#     return render(request, "reports/edit.html", context)


def edit(request, report_id):
    report = Report.objects.get(id=report_id)
    context = {"reports": report}
    return render(request, "reports/index.html", context)


def delete(request, report_id):
    report = Report.objects.get(id=report_id)
    report.delete()
    return render(request, "reports/index.html")


def add(request):
    if request.method == "POST":
        form = YourModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  # Redirect to your index page or any other page
    else:
        form = YourModelForm()
    return render(request, "reports/add.html", {"form": form})
