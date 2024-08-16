from django.shortcuts import render

from .models import Legislation


def index(request):
    legislations = Legislation.objects.all()
    context = {"legislations": legislations}
    return render(request, "legislations/index.html", context)
