# from django.core.cache import cache
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from django.test import RequestFactory
# from django.utils import timezone
# from django.utils.cache import get_cache_key
# 
# from reports.models import Suspect, Report
# 
# 
# @receiver(post_save, sender=Report)
# @receiver(post_delete, sender=Report)
# def invalidate_report_cache(sender, instance, **kwargs):
#     request = RequestFactory().get(
#         f"/reports/detail/{instance.pk}/", HTTP_HOST="localhost:8000"
#     )
#     cache_key = get_cache_key(request)
#     print("invalidating:", cache_key)
#     cache.delete(cache_key)
# 
# 
# @receiver(post_save, sender=Suspect)
# @receiver(post_delete, sender=Suspect)
# def update_last_changed_report(sender, instance, **kwargs):
#     report = instance.report
#     report.last_changed = timezone.now()
#     report.save()
