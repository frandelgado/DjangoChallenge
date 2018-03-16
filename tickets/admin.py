from django.contrib import admin

from solo.admin import SingletonModelAdmin

from .models import Holiday, WorkHourSetting, ServiceCategory, ServiceOrder

admin.site.register(Holiday)
admin.site.register(WorkHourSetting, SingletonModelAdmin)
admin.site.register(ServiceCategory)
admin.site.register(ServiceOrder)
