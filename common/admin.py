from django.contrib import admin

from .models import Tag, Notification, GenericFile

admin.site.register(Tag)
admin.site.register(Notification)
admin.site.register(GenericFile)
