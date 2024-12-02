from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_not_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from DjangoPolls import settings
from reports.models import Suspect, Report


@login_not_required
@never_cache
def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:index")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "accounts/home.html")
        else:
            print("Invalid username or password")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


def index(request):
    suspects_with_warrant = Suspect.objects.filter(is_warrant=True, is_processed=False)[:16]
    announcements = Report.objects.filter(type="Announcement")[:8]
    suspects_processed = Suspect.objects.filter(is_processed=True)[:8]
    context = {"suspects_with_warrant": suspects_with_warrant,
               "announcements": announcements,
               "suspects_processed": suspects_processed, }
    return render(request, "accounts/home.html", context)
