from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from ninja import Router

from reports.models import Report

router = Router(tags=["reports"])


@router.get("/list")
def show(request, count=5):
    """
    :param count: how many reports to show (max 100)
    :return: list of reports {report.pk:report.title}
    """
    if count > 100:
        return
    reports = Report.objects.all()[:count]
    return {report.pk: str(report) for report in reports}


@router.get("/get")
def fetch(request, pk: int):
    report = get_object_or_404(Report, pk=pk)
    return model_to_dict(report)


@router.get("/create")
def create(request, title: str):
    Report.objects.create(title=title, created_by=request.user)
    return
