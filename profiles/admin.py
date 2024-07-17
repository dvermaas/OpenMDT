from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from profiles.models import Profile

# admin.site.register(Profile)
admin.site.register(Profile, SimpleHistoryAdmin)
