from django.contrib import admin

# Register your models here.
from .models import USERTABLE
from .models import PERMISSION

admin.site.register(USERTABLE)
admin.site.register(PERMISSION)