from .models import Notification


def notifications(request):
    return {"notifications": Notification.objects.order_by("-created_at")}
