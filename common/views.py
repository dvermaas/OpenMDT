from django.shortcuts import render


def index(request):
    return render(request, "common/ciot.html")


def announcement(request, pk):
    return render(request, "common/announcement.html")
