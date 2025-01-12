from allauth.account.internal.decorators import login_not_required
from django.core.files.storage import default_storage
from django.http import FileResponse
from django.shortcuts import render

from common.models import GenericFile


def index(request):
    return render(request, "common/ciot.html")

@login_not_required
def downloads(request, pk):
    return FileResponse(default_storage.open(GenericFile.objects.get(id=pk).file.path))
