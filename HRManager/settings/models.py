from django.db import models
from django.contrib.auth.models import User
from django.utils.translation   import gettext_lazy as _
from datetime import time

class Core(models.Model):
     title                     = models.CharField(default=_("default settings") , max_length=220)
     day_shift_hours           = models.IntegerField(_("shift hours"), default=8)
     flexible_start_time       = models.TimeField(_("flexible start time range"))
     flexible_end_time         = models.TimeField(_("flexible end time range"))
     shift_start               = models.TimeField(_("shift start time") , default=time(8,0,0))
     shift_end                 = models.TimeField(_("shift end time") , default=time(4,30,0))
     users_default_image       = models.ImageField(_("default image") , upload_to="media/default/")
     active                    = models.BooleanField(default=True)
     
     
     def __str__(self):
          return self.title
     
     class Meta:
          verbose_name        = _("Core settings")
          verbose_name_plural = _("Core settings")
     
     def save(self , *args, **kwargs):
          for settings_object in Core.objects.all():
               if settings_object.active == True:
                    settings_object.active = False 
                    settings_object.save()
               self.active = True
          super(Core, self).save(*args, **kwargs)
     
     
     