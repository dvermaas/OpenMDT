from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from reports.models import Report, Suspect


@receiver(post_save, sender=Report)
@receiver(post_delete, sender=Report)
def invalidate_report_cache(sender, instance, **kwargs):
    cache_key = f"reports/detail/{instance.pk}"
    cache.delete(cache_key)


@receiver(post_save, sender=Suspect)
@receiver(post_delete, sender=Suspect)
def invalidate_report_cache_on_suspect_change(sender, instance, **kwargs):
    cache_key = f"reports/detail/{instance.report.pk}"
    cache.delete(cache_key)
