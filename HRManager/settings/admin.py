from django.contrib import admin
from .models import Core
# Register your models here.

class Core_design(admin.ModelAdmin):
     list_display   = ['id' , 'title' , 'day_shift_hours' , 'flexible_start_time' , 'flexible_end_time' , 'shift_start' , 'shift_end']
     search_fields  = ['title']
     list_filter    = ['day_shift_hours']


admin.site.register(Core , Core_design)