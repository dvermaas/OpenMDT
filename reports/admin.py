from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Report, Evidence, Suspect, Charge


class SuspectInline(admin.TabularInline):
    model = Suspect
    extra = 1
    # fields = ["profile"]
    readonly_fields = ["created_at"]
    classes = ["collapse"]


class ReportAdmin(SimpleHistoryAdmin):
    list_display = (
        "id",
        "is_active",
        "title",
        "created_by",
        "created_at",
        "last_modified_at",
    )
    inlines = [SuspectInline]


admin.site.register(Report, ReportAdmin)
admin.site.register(Evidence)
admin.site.register(Charge)
