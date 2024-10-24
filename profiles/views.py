from collections import Counter

from django.core.paginator import Paginator
from django.http import QueryDict
from django.shortcuts import render, get_object_or_404

from profiles.forms import ProfileInfoForm, ProfileSummaryForm, ProfilePictureForm
from profiles.models import Profile
from reports.models import Charge


def index(request):
    return render(request, "profiles/index.html")


def table(request):
    profiles = Profile.objects.order_by("-created_at")
    paginator = Paginator(profiles, 30)
    page = paginator.get_page(request.GET.get("page", 1))
    context = {"profiles": page}
    return render(request, "profiles/partials/table.html", context)


def detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    charges = Counter(
        str(charge) for charge in Charge.objects.filter(suspect__profile=profile)
    )
    context = {"profile": profile, "charges": charges}
    return render(request, "profiles/detail.html", context)


def detail_picture_form(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    context = {"profile": profile}
    if request.method == "POST":
        form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return render(request, "profiles/partials/picture.html", context)
    context["form"] = ProfilePictureForm(instance=profile)
    return render(request, "profiles/partials/picture-form.html", context)


def detail_info_form(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    context = {"profile": profile}
    if request.method == "PUT":
        data = QueryDict(request.body)
        form = ProfileInfoForm(data, instance=profile)
        if form.is_valid():
            form.save()
            return render(request, "profiles/partials/info.html", context)
    context["form"] = ProfileInfoForm(instance=profile)
    return render(request, "profiles/partials/info-form.html", context)


def detail_summary_form(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    context = {"profile": profile}
    if request.method == "PUT":
        data = QueryDict(request.body)
        form = ProfileSummaryForm(data, instance=profile)
        if form.is_valid():
            form.save()
            return render(request, "profiles/partials/summary.html", context)
    context["form"] = ProfileSummaryForm(instance=profile)
    return render(request, "profiles/partials/summary-form.html", context)


def delete(request, pk):
    report = Profile.objects.get(id=pk)
    report.delete()
    return index(request)
