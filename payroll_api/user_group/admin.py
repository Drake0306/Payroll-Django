from django.contrib import admin

from .models import UserGroup, UserPermission, UserAccounts

# Register your models here.
admin.site.register(UserGroup)
admin.site.register(UserPermission)
admin.site.register(UserAccounts)