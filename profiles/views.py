from django.shortcuts import render

from profiles.models import Profile


def index(request):
    latest_profile_list = Profile.objects.order_by("-created_at")[:]
    context = {"latest_profile_list": latest_profile_list}
    return render(request, "profiles/index.html", context)


def detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    context = {"profile": profile}
    return render(request, "profiles/detail.html", context)


def delete(request, profile_id):
    report = Profile.objects.get(id=profile_id)
    report.delete()
    return index(request)
