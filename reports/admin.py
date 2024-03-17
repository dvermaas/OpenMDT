from django.contrib import admin

from .models import Report, Tag, Evidence


class ReportAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_by", "created_at", "last_modified_at")


admin.site.register(Report, ReportAdmin)
admin.site.register(Tag)
admin.site.register(Evidence)
