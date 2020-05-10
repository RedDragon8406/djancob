from django.contrib import admin

from masters.models import Master

class MasterAdmin(admin.ModelAdmin):
    list_display = ['__str__','description']
    class Meta:
        model = Master

admin.site.register(Master,MasterAdmin)