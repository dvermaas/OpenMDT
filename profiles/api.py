from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from ninja import Router

from profiles.models import Profile

router = Router(tags=["profiles"])


@router.get("/list")
def show(request, n: int = 5):
    """
    :param n: how many reports to show (max 100)
    :return: list of reports {report.pk:report.title}
    """
    if n > 100:
        n = 100
    profiles = Profile.objects.all()[:n]
    return {profile.pk: str(profile) for profile in profiles}


@router.get("/get")
def fetch(request, pk: int):
    profile = get_object_or_404(Profile, pk=pk)
    return model_to_dict(profile)


@router.get("/create")
def create(request, first_name: str, last_name: str):
    Profile.objects.create(name=first_name, surname=last_name)
    return
