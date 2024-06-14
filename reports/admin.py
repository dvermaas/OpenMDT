from django.contrib import admin

from .models import Report, Evidence, Charge, Suspect


class SuspectInline(admin.TabularInline):
    model = Suspect
    extra = 1
    # fields = ["profile"]
    readonly_fields = ["created_at"]
    classes = ["collapse"]


class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "created_by",
        "created_at",
        "last_modified_at",
    )
    inlines = [SuspectInline]


admin.site.register(Report, ReportAdmin)
admin.site.register(Evidence)
admin.site.register(Charge)
