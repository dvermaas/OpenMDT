from django.contrib import admin

from .models import Tag, Notification, Announcement

admin.site.register(Tag)
admin.site.register(Notification)
admin.site.register(Announcement)
