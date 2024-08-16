from django.shortcuts import render

from .models import Legislation


def index(request):
    legislations = Legislation.objects.all().order_by("title")
    context = {"legislations": legislations}
    return render(request, "legislations/index.html", context)
