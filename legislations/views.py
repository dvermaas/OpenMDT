from django.shortcuts import render

from . import forms
from .models import Legislation


def index(request):
    legislations = Legislation.objects.all().order_by("title")
    context = {"legislations": legislations, "form": forms.LegislationSearchForm()}
    return render(request, "legislations/index.html", context)
