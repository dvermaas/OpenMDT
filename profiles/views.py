from django.shortcuts import render

from profiles.models import Profile


def index(request):
    latest_profile_list = Profile.objects.order_by("-created_at")[:]
    context = {"latest_profile_list": latest_profile_list}
    return render(request, "profiles/index.html", context)
