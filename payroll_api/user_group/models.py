from django.db import models

# Create your models here.

class UserGroup(models.Model):
    name = models.CharField(max_length=250)
    #master
    master_add = models.BooleanField(default=False)
    master_delete = models.BooleanField(default=False)
    master_update = models.BooleanField(default=False)
    master_list = models.BooleanField(default=True)
    #user
    user_add = models.BooleanField(default=False)
    user_delete = models.BooleanField(default=False)
    user_update = models.BooleanField(default=False)
    user_list = models.BooleanField(default=True)
    #org
    org_add = models.BooleanField(default=False)
    org_delete = models.BooleanField(default=False)
    org_update = models.BooleanField(default=False)
    org_list = models.BooleanField(default=True)
    #branch
    branch_add = models.BooleanField(default=False)
    branch_delete = models.BooleanField(default=False)
    branch_update = models.BooleanField(default=False)
    branch_list = models.BooleanField(default=True)
    #work-order
    work_order_add = models.BooleanField(default=False)
    work_order_delete = models.BooleanField(default=False)
    work_order_update = models.BooleanField(default=False)
    work_order_list = models.BooleanField(default=True)
    #billing
    billing_add = models.BooleanField(default=False)
    billing_delete = models.BooleanField(default=False)
    billing_update = models.BooleanField(default=False)
    billing_list = models.BooleanField(default=True)
    #payment
    payment_add = models.BooleanField(default=False)
    payment_delete = models.BooleanField(default=False)
    payment_update = models.BooleanField(default=False)
    payment_list = models.BooleanField(default=True)
    status = models.BooleanField(default=True)

class UserPermission(models.Model):
    user_id = models.IntegerField()
    user_group_id = models.IntegerField()
    org_id = models.IntegerField(blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    head_org_user = models.BooleanField(default=False)
    head_branch_user = models.BooleanField(default=False)
    super_user = models.BooleanField(default=False)
    created = models.DateField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)

class UserAccounts(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    last_login = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    created = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.username}"

