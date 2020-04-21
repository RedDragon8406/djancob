from django.contrib import admin

from .models import Course

class MasterAdmin(admin.ModelAdmin):
    list_display = ['__str__','topic','price','master','level','condition']
    class Meta:
        model = Course

admin.site.register(Course,MasterAdmin)