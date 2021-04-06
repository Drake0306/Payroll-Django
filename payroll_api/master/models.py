from django.db import models

# Create your models here.

class site(models.Model):
    name = models.CharField(max_length=250,blank=False,null=False )

class department(models.Model):
    name = models.CharField(max_length=250,blank=False,null=False)

class designation(models.Model):
    name = models.CharField(max_length=250,blank=False,null=False)

class bank(models.Model):
    name = models.CharField(max_length=250,blank=False,null=False)

class state(models.Model):
    name = models.CharField(max_length=250,blank=False,null=False)


class employee(models.Model):
    # Personal Information
    employee_name                   = models.CharField(max_length=250,blank=False,null=False)
    gender                          = models.CharField(max_length=250,blank=False,null=False)
    marital_status                  = models.CharField(max_length=250,blank=False,null=False)
    # date_of_birth                   = models.DateField(auto_now=False, auto_now_add=False,blank=False, null=False)
    date_of_birth                   = models.CharField(max_length=250,blank=False,null=False)
    father_name                     = models.CharField(max_length=250,blank=False,null=False)
    working_status                  = models.CharField(max_length=250,blank=True,null=True)
    date_of_joining                 = models.CharField(max_length=250,blank=False,null=False)
    date_of_resigning               = models.CharField(max_length=250,blank=False,null=False)

    # Residential Address
    residential_address_line_one    = models.CharField(max_length=250,blank=False,null=False)
    residential_address_line_two    = models.CharField(max_length=250,blank=True,null=True)
    residential_area                = models.CharField(max_length=250,blank=True,null=True)
    residential_landmark            = models.CharField(max_length=250,blank=True,null=True)
    residential_post_office         = models.CharField(max_length=250,blank=True,null=True)
    residential_police_station      = models.CharField(max_length=250,blank=True,null=True)
    residential_city_village        = models.CharField(max_length=250,blank=True,null=True)
    residential_district            = models.CharField(max_length=250,blank=True,null=True)
    residential_state               = models.CharField(max_length=250,blank=False,null=False)
    residential_country             = models.CharField(max_length=250,blank=False,null=False)
    residential_pin_code            = models.CharField(max_length=250,blank=False,null=False)

    # Permanent Address
    permanent_address_line_one      = models.CharField(max_length=250,blank=False,null=False)
    permanent_address_line_two      = models.CharField(max_length=250,blank=True,null=True)
    permanent_area                  = models.CharField(max_length=250,blank=True,null=True)
    permanent_landmark              = models.CharField(max_length=250,blank=True,null=True)
    permanent_post_office           = models.CharField(max_length=250,blank=True,null=True)
    permanent_police_station        = models.CharField(max_length=250,blank=True,null=True)
    permanent_city_village          = models.CharField(max_length=250,blank=True,null=True)
    permanent_district              = models.CharField(max_length=250,blank=True,null=True)
    permanent_state                 = models.CharField(max_length=250,blank=False,null=False)
    permanent_country               = models.CharField(max_length=250,blank=False,null=False)
    permanent_pin_code               = models.CharField(max_length=250,blank=False,null=False)

    # contact and address proof
    contact_address_proof_email                 = models.CharField(max_length=250,blank=True,null=True)
    contact_address_proof_mobile_one            = models.CharField(max_length=250,blank=False,null=False)
    contact_address_proof_mobile_two            = models.CharField(max_length=250,blank=True,null=True)
    contact_address_proof_phone                 = models.CharField(max_length=250,blank=True,null=True)
    contact_address_proof_contact_person_name   = models.CharField(max_length=250,blank=True,null=True)
    contact_address_proof_contact_person_no     = models.CharField(max_length=250,blank=True,null=True)
    contact_address_proof_aadhar_no             = models.CharField(max_length=250,blank=True,null=True)
    contact_address_proof_pan                   = models.CharField(max_length=250,blank=True,null=True)

    # More Data
    work_man_no_int                 = models.CharField(max_length=250,blank=False,null=False)
    site                            = models.CharField(max_length=250,blank=False,null=False)
    department                      = models.CharField(max_length=250,blank=False,null=False)
    designation                     = models.CharField(max_length=250,blank=False,null=False)
    pf_applicable                   = models.CharField(max_length=250,blank=False,null=False)
    uan_p_f_no                      = models.CharField(max_length=250,blank=True,null=True)
    esic_applicable                 = models.CharField(max_length=250,blank=False,null=False)
    esic_no                         = models.CharField(max_length=250,blank=True,null=True)
    reverse_pf_esi                  = models.CharField(max_length=250,blank=False,null=False)
    bonus_per_month                 = models.CharField(max_length=250,blank=False,null=False)

    #  Security
    work_order_no                   = models.CharField(max_length=250,blank=False,null=False)
    gate_pass_no                    = models.CharField(max_length=250,blank=True,null=True)
    gate_pass_due_date              = models.CharField(max_length=250,blank=True,null=True)
    safety_pass_no                  = models.CharField(max_length=250,blank=True,null=True)
    safety_pass_due_date            = models.CharField(max_length=250,blank=True,null=True)
    rfid_no                         = models.CharField(max_length=250,blank=True,null=True)
    rfid_due_date                   = models.CharField(max_length=250,blank=True,null=True)

    # bank details
    bank_name                       = models.CharField(max_length=250,blank=False,null=False)
    bank_branch                     = models.CharField(max_length=250,blank=False,null=False)
    a_c_no                          = models.CharField(max_length=250,blank=False,null=False)
    ifsc                            = models.CharField(max_length=250,blank=False,null=False)
    a_c_holder_name                 = models.CharField(max_length=250,blank=False,null=False)

    # Addition and deduction
    basic                           = models.FloatField(blank=False, null=False,default=0.00)
    pay_rate                        = models.FloatField(blank=False, null=False,default=0.00)
    actual_rate                     = models.FloatField(blank=False, null=False,default=0.00)
    da                              = models.FloatField(blank=False, null=False,default=0.00)
    hra_float                       = models.FloatField(blank=False, null=False,default=0.00)
    ca_float                        = models.FloatField(blank=False, null=False,default=0.00)
    food_float                      = models.FloatField(blank=False, null=False,default=0.00)
    miscellaneous_float             = models.FloatField(blank=False, null=False,default=0.00)
    old_DA                          = models.FloatField(blank=False, null=False,default=0.00)

    payment_mode                    = models.CharField(max_length=250,blank=False,null=False)
    sunday_payable                  = models.CharField(max_length=250,blank=False,null=False)

    hra                             = models.CharField(max_length=250,blank=True,null=True)
    Food                            = models.CharField(max_length=250,blank=True,null=True)
    ca                              = models.CharField(max_length=250,blank=True,null=True)
    miscellaneous                   = models.CharField(max_length=250,blank=True,null=True)
    leave_days                      = models.IntegerField(blank=True, null=True)

    salary_on_attendance            = models.CharField(max_length=250,blank=True,null=True)
    over_time_applicable            = models.CharField(max_length=250,blank=True,null=True)
    over_time_on                    = models.CharField(max_length=250,blank=True,null=True)
    mr_over_time_hours              = models.IntegerField(blank=True, null=True)

    # created_at                      = models.DateField(auto_now=True, auto_now_add=False)

class pincode(models.Model):
    office_name = models.CharField(max_length=250,blank=False,null=False)
    pin_code = models.CharField(max_length=250,blank=False,null=False)
    district = models.CharField(max_length=250,blank=False,null=False)
    state_name = models.CharField(max_length=250,blank=False,null=False)


class holiday_list(models.Model):
    holiday_date = models.CharField(max_length=250,blank=False,null=False)
    holiday_type = models.CharField(max_length=250,blank=False,null=False)


class attendance_for_user(models.Model):
    employee_id = models.CharField(max_length=250,blank=False,null=False)
    date = models.DateField(auto_now=False, auto_now_add=False, blank=False,null=False)
    attendance = models.CharField(max_length=250,blank=False,null=False)

class get_persent(models.Model):
    pf = models.CharField(max_length=250,blank=False,null=False)
    esi = models.CharField(max_length=250,blank=False,null=False)

class payslip_per_user(models.Model):
    employee_id = models.CharField(max_length=250,blank=False,null=False)
    total_working_day = models.CharField(max_length=250,blank=False,null=False)
    date = models.DateField(auto_now=False, auto_now_add=False, blank=False,null=False)
    rate = models.CharField(max_length=250,blank=False,null=False)
    total_amount = models.CharField(max_length=250,blank=False,null=False)
    site_amount = models.CharField(max_length=250,blank=False,null=False)
    pf_deduction = models.CharField(max_length=250,blank=False,null=False)
    pf_amount = models.CharField(max_length=250,blank=False,null=False)
    esi_deduction = models.CharField(max_length=250,blank=False,null=False)
    esi_amount = models.CharField(max_length=250,blank=False,null=False)
    attendance_type = models.CharField(max_length=250,blank=False,null=False)