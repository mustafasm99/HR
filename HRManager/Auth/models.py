from django.db import models
from django.utils.translation   import gettext_lazy as _
from django.contrib.auth.models import User , AbstractUser , AbstractBaseUser


# over Right the user model to creat

class department(models.Model):
     name      = models.CharField(max_length=120 , verbose_name=_("name"))
     
     def __str__(self):
          return self.name

     class Meta:
          verbose_name        = _("department")
          verbose_name_plural = _("department")

class employe(AbstractUser):
     image          = models.ImageField(_("employe image"), upload_to="employe-imges/", height_field=None, width_field=None, max_length=5 , null=True , blank=True)
     department     = models.ForeignKey("department" ,verbose_name=_("employe department") , on_delete=models.CASCADE , null=True , blank=True) 

     def __str__(self):
          return self.username
     

class Attendees(models.Model):
     user      = models.ForeignKey(to=employe , on_delete=models.SET_NULL , null=True , blank=True , verbose_name=_("User"))
     in_time   = models.TimeField(verbose_name=_("punch in  time") , auto_now_add=True)
     out_time  = models.TimeField(verbose_name=_("punch out time") , auto_created=True)
     date      = models.DateField(verbose_name=_("date") , auto_now_add=True)
     type      = models.CharField(_("type"), max_length=120 , default=_("day shift"))
     
     def __str__(self):
          return self.user.username
     
     def get_user_attendess(user):
          return Attendees.objects.filter(user = user).all()