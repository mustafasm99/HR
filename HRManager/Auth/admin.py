from django.contrib import admin
from .models import department , employe , Attendees
from django.utils.translation   import gettext_lazy as _


class department_design(admin.ModelAdmin):
     list_display = ["id" , "name"]
     search_fields = ["name"]

class employe_display(admin.ModelAdmin):
     list_display        = ["id" , "username" ,"email" ,"last_login"]
     list_display_links  = ["username"]
     search_fields       = ["username" , "email"]


class Attendees_disply(admin.ModelAdmin):
     list_display        = ['id', "user"  , "in_time" , "out_time" , "date" , "type"]
     search_fields       = ["id", "user__username"  ,"date"]
     list_display_links  = ["id" , "user"]
     
admin.site.register(department , department_design)
admin.site.register(employe , employe_display)
admin.site.register(Attendees , Attendees_disply)