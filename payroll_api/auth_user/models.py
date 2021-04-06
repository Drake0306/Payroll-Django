from django.db import models

# Create your models here.
class USERTABLE(models.Model):
    name = models.CharField(max_length=250,blank=True, null=True)
    user_name = models.CharField(max_length=250,blank=True, null=True)
    password = models.CharField(max_length=250,blank=True, null=True)
    branch = models.CharField(max_length=250,blank=True, null=True)
    user_role = models.CharField(max_length=250,blank=True, null=True)
    admin = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)



class PERMISSION(models.Model):
    name = models.CharField(max_length=250)
    admin = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)
    master_show = models.BooleanField(default=False)
    master_add = models.BooleanField(default=False)
    master_edit = models.BooleanField(default=False)
    master_status = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    