from django.contrib import admin

from .models import Report, Tag, Evidence, Charge, Suspect


class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "created_by",
        "created_at",
        "last_modified_at",
    )


class SuspectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "report",
        "profile",
        "created_at",
    )


admin.site.register(Report, ReportAdmin)
admin.site.register(Suspect, SuspectAdmin)
admin.site.register(Evidence)
admin.site.register(Charge)
