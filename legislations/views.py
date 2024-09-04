from django.shortcuts import render

from . import forms
from .models import Legislation


def index(request):
    legislations = Legislation.objects.all().order_by("title")
    context = {"legislations": legislations, "form": forms.LegislationSearchForm()}

    if request.POST:
        print("borpa", request.META.get("REMOTE_ADDR"))
        print("spin", request.META.get("HTTP_X_FORWARDED_FOR"))
        query = request.POST.get("query")
        legislations = legislations.filter(title__icontains=query)
        return render(
            request,
            "legislations/partials/filtered.html",
            {"legislations": legislations},
        )

    return render(request, "legislations/index.html", context)
