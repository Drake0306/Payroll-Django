from django.contrib import admin
from .models import site
from .models import department 
from .models import designation
from .models import bank
from .models import state
from .models import employee



# Register your models here.

admin.site.register(site)
admin.site.register(department)
admin.site.register(designation)
admin.site.register(bank)
admin.site.register(state)
admin.site.register(employee)
