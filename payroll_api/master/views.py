from django.shortcuts import render
from django.db import connection
from django.db.models import Q


# Create your views here.

# django rest import
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta, date

# serilizer 
from .serializers import siteSerializer
from .serializers import departmentSerializer
from .serializers import designationSerializer
from .serializers import bankSerializer
from .serializers import stateSerializer

# model
from auth_user.models import USERTABLE
from .models import site
from .models import department
from .models import designation
from .models import bank
from .models import state
from .models import employee
from .models import pincode
from .models import holiday_list
from .models import attendance_for_user
from .models import payslip_per_user
from .models import get_persent


@api_view(['GET'])
def url_data(request):
    data = {
        'login': 'api/log-in',

        'MASTER': '↴',

        'umo': 'api/umo/',
        'umo-add': 'api/umo-add',
        'umo-update': 'api/umo-update/<int:id>',
        'umo-update-list': 'api/umo-update-list/<int:id>',
        'umo-update-status': 'api/umo-update-status/<int:id>',

        
    }
    return Response(data)

# umo list
@api_view(['GET'])
def ListUmo(request):
    UmoListData = UMO.objects.all().order_by('-id')
    UMOSerializerData = UMOSerializer(UmoListData, many=True)
    return Response(UMOSerializerData.data)

# umo insert
@api_view(['POST'])
def addUmo(request):
    # check if data is present or not
    UMOData = UMO.objects.filter(umo_name= request.data.get("umo_name")).exists()
    if UMOData == True:
        status ={
            'status': 'exist'
        }
        return Response( status )
    else:
        # UMO create
        UMOSerializerData = UMOSerializer(data= request.data)
        if UMOSerializerData.is_valid():
            UMOSerializerData.save()
            return Response(UMOSerializerData.data)
        else:
            status ={
            'status': '400'
        }
        return Response( status )


# Update umo
@api_view(['POST'])
def updateUom(request,id):
    # Getting data for update
    UMOData = UMO.objects.get(id= id)
    UMODataCheck = UMO.objects.filter(umo_name= request.data.get("umo_name")).exclude(id= id).exists()
    if UMODataCheck == False:
        # for initilising data
        UMOrSerializerData = UMOSerializer(data= request.data)
        # for validating data
        if UMOrSerializerData.is_valid():
            # for saving new data
            UMOData.umo_name = request.data.get("umo_name")
            UMOData.abbreviation = request.data.get("umo_name")
            # UMOData.status = request.data.get("status")
            UMOData.save()
            return Response(UMOrSerializerData.data)
        else:
            status ={
                'status': '400'
            }
            return Response(status)
    else:
        status ={
                'status': 'exist'
            }
        return Response(status)


# Update-status umo
@api_view(['GET'])
def updateUomStatus(request,id):
    # Getting data for update
    UMODataCheck = UMO.objects.get(id= id)
    print(UMODataCheck.status)
    # for initilising data
    UMOrSerializerData = UMOSerializer(UMODataCheck , many=False)
    # for saving new data
    if UMODataCheck.status == True:
        UMODataCheck.status = False
    else:
        UMODataCheck.status = True
    UMODataCheck.save()
    status = UMODataCheck.status
    return Response(status)


# Update-view umo
@api_view(['GET'])
def updateListUom(request,id):
    # Getting data for update
    UMOData = UMO.objects.get(id= id)
    UMOSerializerData = UMOSerializer(UMOData, many=False)
    return Response(UMOSerializerData.data)


@api_view(['GET'])
def ListSite(request):
    SiteList = site.objects.all().order_by('-id')
    siteSerializerData = siteSerializer(SiteList, many=True)
    return Response(siteSerializerData.data)


@api_view(['POST'])
def addSITE(request):
    SITEData = site.objects.filter(name= request.data.get("name")).exists()
    if SITEData == True:
        status ={
            'status': 'exist'
        }
        return Response( status )
    else:
        siteSerializerData = siteSerializer(data = request.data)
        if siteSerializerData.is_valid():
            siteSerializerData.save()
            return Response(siteSerializerData.data)
        else:
            status ={
                'status': '400'
            }
            return Response( status )


@api_view(['GET'])
def updateListSite(request,id):
    SITEData = site.objects.get(id= id)
    siteSerializerData = siteSerializer(SITEData, many=False)
    return Response(siteSerializerData.data)


@api_view(['POST'])
def updateSite(request,id):
    # Getting data for update
    SITEData = site.objects.get(id= id)
    SITEDataCheck = site.objects.filter(name= request.data.get("name")).exclude(id= id).exists()
    if SITEDataCheck == False:
        # for initilising data
        siteSerializerData = siteSerializer(data= request.data)
        # for validating data
        if siteSerializerData.is_valid():
            # for saving new data
            SITEData.name = request.data.get("name")
            SITEData.save()
            return Response(siteSerializerData.data)
        else:
            status ={
                'status': '400'
            }
            return Response(status)
    else:
        status ={
                'status': 'exist'
            }
        return Response(status)



@api_view(['GET'])
def Listdepartment(request):
    departmentList = department.objects.all().order_by('-id')
    departmentSerializerData = departmentSerializer(departmentList, many=True)
    return Response(departmentSerializerData.data)



@api_view(['POST'])
def adddepartment(request):
    DEPARTMENTData = department.objects.filter(name= request.data.get("name")).exists()
    if DEPARTMENTData == True:
        status ={
            'status': 'exist'
        }
        return Response( status )
    else:
        departmentSerializerData = departmentSerializer(data = request.data)
        if departmentSerializerData.is_valid():
            departmentSerializerData.save()
            return Response(departmentSerializerData.data)
        else:
            status ={
                'status': '400'
            }
            return Response( status )



@api_view(['GET'])
def updateListdepartment(request,id):
    DEPARTMENTData = department.objects.get(id= id)
    departmentSerializerData = departmentSerializer(DEPARTMENTData, many=False)
    return Response(departmentSerializerData.data)


@api_view(['POST'])
def updatedepartment(request,id):
    # Getting data for update
    DEPARTMENTData = department.objects.get(id= id)
    DEPARTMENTDataCheck = department.objects.filter(name= request.data.get("name")).exclude(id= id).exists()
    if DEPARTMENTDataCheck == False:
        # for initilising data
        departmentSerializerData = departmentSerializer(data= request.data)
        # for validating data
        if departmentSerializerData.is_valid():
            # for saving new data
            DEPARTMENTData.name = request.data.get("name")
            DEPARTMENTData.save()
            return Response(departmentSerializerData.data)
        else:
            status ={
                'status': '400'
            }
            return Response(status)
    else:
        status ={
                'status': 'exist'
            }
        return Response(status)



@api_view(['GET'])
def Listdesignation(request):
    designationList = designation.objects.all().order_by('-id')
    designationSerializer_data = designationSerializer(designationList, many=True)
    return Response(designationSerializer_data.data)
    

@api_view(['POST'])
def adddesignation(request):
    designation_data = designation.objects.filter(name= request.data.get("name")).exists()
    if designation_data == True:
        status ={
            'status': 'exist'
        }
    else:
        designationSerializer_data = designationSerializer(data = request.data)
        if designationSerializer_data.is_valid():
            designationSerializer_data.save()
            return Response(designationSerializer_data.data)
        else:
            status= {
                'status':'400'
            }
            return Response( status )


@api_view(['GET'])
def updateListdesignation(request,id):
    designation_data = designation.objects.get(id= id)
    designationSerializer_data = designationSerializer(designation_data, many=False)
    return Response(designationSerializer_data.data)


@api_view(['POST'])
def updatedesignation(request,id):
    # Getting data for update
    designation_data = designation.objects.get(id= id)
    designationCheck = designation.objects.filter(name= request.data.get("name")).exclude(id= id).exists()
    if designationCheck == False:
        # for initilising data
        designationSerializerData = designationSerializer(data= request.data)
        # for validating data
        if designationSerializerData.is_valid():
            # for saving new data
            designation_data.name = request.data.get("name")
            designation_data.save()
            return Response(designationSerializerData.data)
        else:
            status ={
                'status': '400'
            }
            return Response(status)
    else:
        status ={
                'status': 'exist'
            }
        return Response(status)



@api_view(['GET'])
def bankList(request):
    bank_list = bank.objects.all().order_by('-id')
    bankSerializer_data = bankSerializer(bank_list, many=True)
    return Response(bankSerializer_data.data)



@api_view(['POST'])
def addbank(request):
    # checking data 
    bank_data_check = bank.objects.filter(name= request.data.get("name")).exists()
    if bank_data_check == True:
        status= {
            'status' : "400"
        }
        return Response( status )
    else:
        bankSerializer_data = bankSerializer(data = request.data)
        if bankSerializer_data.is_valid():
            bankSerializer_data.save()
            return Response(bankSerializer_data.data)
        else:
            status={
                'status' : '400'
            }
            return Response( status )



@api_view(['GET'])
def updateListbank(request,id):
    bank_fetch = bank.objects.get(id= id)
    bankSerializer_data = bankSerializer(bank_fetch, many=False)
    return Response(bankSerializer_data.data)



@api_view(['POST'])
def updatebank(request,id):
    # Getting data for update
    bank_data = bank.objects.get(id= id)
    bankCheck = bank.objects.filter(name= request.data.get("name")).exclude(id= id).exists()
    if bankCheck == False:
        # for initilising data
        bankSerializerData = bankSerializer(data= request.data)
        # for validating data
        if bankSerializerData.is_valid():
            # for saving new data
            bank_data.name = request.data.get("name")
            bank_data.save()
            return Response(bankSerializerData.data)
        else:
            status ={
                'status': '400'
            }
            return Response(status)
    else:
        status ={
                'status': 'exist'
            }
        return Response(status)



@api_view(['GET'])
def stateList(request):
    state_list = state.objects.all().order_by('-id')
    stateSerializer_data = stateSerializer(state_list, many=True)
    return Response(stateSerializer_data.data)

@api_view(['GET'])
def PincodeList(request):
    PincodeData = pincode.objects.all().order_by('-id')
    tag = []
    for index in PincodeData:
        tag.append({
            'id': index.id,
            'office_name': index.office_name,
            'pin_code' : index.pin_code,
            'district': index.district,
            'state_name' : index.state_name,
        })
    return Response(tag)



@api_view(['POST'])
def addstate(request):
    # checking data 
    state_data_check = state.objects.filter(name= request.data.get("name")).exists()
    if state_data_check == True:
        status= {
            'status' : "400"
        }
        return Response( status )
    else:
        stateSerializer_data = stateSerializer(data = request.data)
        if stateSerializer_data.is_valid():
            stateSerializer_data.save()
            return Response(stateSerializer_data.data)
        else:
            status={
                'status' : '400'
            }
            return Response( status )



@api_view(['GET'])
def updateListstate(request,id):
    state_fetch = state.objects.get(id= id)
    stateSerializer_data = stateSerializer(state_fetch, many=False)
    return Response(stateSerializer_data.data)



@api_view(['POST'])
def updatestate(request,id):
    # Getting data for update
    state_data = state.objects.get(id= id)
    stateCheck = state.objects.filter(name= request.data.get("name")).exclude(id= id).exists()
    if stateCheck == False:
        # for initilising data
        stateSerializerData = stateSerializer(data= request.data)
        # for validating data
        if stateSerializerData.is_valid():
            # for saving new data
            state_data.name = request.data.get("name")
            state_data.save()
            return Response(stateSerializerData.data)
        else:
            status ={
                'status': '400'
            }
            return Response(status)
    else:
        status ={
                'status': 'exist'
            }
        return Response(status)


@api_view(['GET'])
def employeeList(request):
    employee_data = employee.objects.all().order_by('-id')
    tag = []
    for index in employee_data:
        tag.append({
            'id': index.id,
            'employee_name': index.employee_name,
            'working_status' : index.working_status,
            'residential_address_line_one': index.residential_address_line_one,
            'work_man_no_int' : index.work_man_no_int,
            'site': index.site,
            'department' : index.department,
            'designation': index.designation,
            'pay_rate' : index.pay_rate,
        })
    return Response(tag)

@api_view(['POST'])
def addemployee(request):
    employee_add = employee()
    employee_add.employee_name = request.data.get('employee_name')
    employee_add.gender = request.data.get('gender')
    employee_add.marital_status = request.data.get('marital_status')
    employee_add.date_of_birth = request.data.get('dob_date')
    employee_add.father_name = request.data.get('fathers_name')
    employee_add.working_status = request.data.get('working_status')
    employee_add.date_of_joining = request.data.get('date_of_joining')
    employee_add.date_of_resigning = request.data.get('date_of_resigning')

    employee_add.residential_address_line_one = request.data.get('address_line_1')
    employee_add.residential_address_line_two = request.data.get('address_line_2')
    employee_add.residential_area = request.data.get('area')
    employee_add.residential_landmark = request.data.get('landmark')
    employee_add.residential_post_office = request.data.get('post_office')
    employee_add.residential_police_station = request.data.get('police_station')
    employee_add.residential_city_village = request.data.get('city_village')
    employee_add.residential_district = request.data.get('district')
    employee_add.residential_state = request.data.get('state')
    employee_add.residential_country = request.data.get('country')
    employee_add.residential_pin_code = request.data.get('pin_code')
    
    employee_add.permanent_address_line_one = request.data.get('address_line_1_permanent')
    employee_add.permanent_address_line_two = request.data.get('address_line_2_permanent')
    employee_add.permanent_area = request.data.get('area_permanent')
    employee_add.permanent_landmark = request.data.get('landmark_permanent')
    employee_add.permanent_post_office = request.data.get('post_office_permanent')
    employee_add.permanent_police_station = request.data.get('police_station_permanent')
    employee_add.permanent_city_village = request.data.get('city_village_permanent')
    employee_add.permanent_district = request.data.get('district_permanent')
    employee_add.permanent_state = request.data.get('state_permanent')
    employee_add.permanent_country = request.data.get('country_permanent')
    employee_add.permanent_pin_code = request.data.get('pin_code_permanent')

    employee_add.contact_address_proof_email = request.data.get('email')
    employee_add.contact_address_proof_mobile_one = request.data.get('mobile_1')
    employee_add.contact_address_proof_mobile_two = request.data.get('mobile_2')
    employee_add.contact_address_proof_phone = request.data.get('phone')
    employee_add.contact_address_proof_contact_person_name = request.data.get('contact_person_name')
    employee_add.contact_address_proof_contact_person_no = request.data.get('contact_person_no')
    employee_add.contact_address_proof_aadhar_no = request.data.get('aadhar_no')
    employee_add.contact_address_proof_pan = request.data.get('pan')

    employee_add.work_man_no_int = request.data.get('work_man_no')
    employee_add.site = request.data.get('site')
    employee_add.department = request.data.get('department')
    employee_add.designation = request.data.get('designation')
    employee_add.pf_applicable = request.data.get('pf_applicable')
    employee_add.uan_p_f_no = request.data.get('uan')
    employee_add.esic_applicable = request.data.get('esic_applicable')
    employee_add.esic_no = request.data.get('esic_no')
    employee_add.reverse_pf_esi = request.data.get('reverse_pf_esi')
    employee_add.bonus_per_month = request.data.get('bonus_per_month')

    employee_add.work_order_no = request.data.get('work_order_no')
    employee_add.gate_pass_no = request.data.get('gate_pass_no')
    employee_add.gate_pass_due_date = request.data.get('gate_pass_due_date')
    employee_add.safety_pass_no = request.data.get('safety_pass_no')
    employee_add.safety_pass_due_date = request.data.get('safety_pass_due_date')
    employee_add.rfid_no = request.data.get('rfid_no')
    employee_add.rfid_due_date = request.data.get('rfid_due_date')

    employee_add.bank_name = request.data.get('bank_name')
    employee_add.bank_branch = request.data.get('bank_branch')
    employee_add.a_c_no = request.data.get('account_no')
    employee_add.ifsc = request.data.get('ifsc_code')
    employee_add.a_c_holder_name = request.data.get('account_holder_name')

    employee_add.basic = request.data.get('basic')
    employee_add.pay_rate = request.data.get('pay_rate')
    employee_add.actual_rate = request.data.get('actual_rate')
    employee_add.da = request.data.get('da')
    employee_add.hra_float = request.data.get('hra')
    employee_add.ca_float = request.data.get('ca')
    employee_add.food_float = request.data.get('food')
    employee_add.miscellaneous_float = request.data.get('miscellaneous')
    employee_add.old_DA = request.data.get('old_da')
    employee_add.payment_mode = request.data.get('payment_mode')
    employee_add.sunday_payable = request.data.get('sunday_payable')
    employee_add.hra = request.data.get('hra_check')
    employee_add.Food = request.data.get('food_check')
    employee_add.ca = request.data.get('ca_check')
    employee_add.miscellaneous = request.data.get('miscellaneous_check')
    employee_add.leave_days = request.data.get('leave_days')
    employee_add.salary_on_attendance = request.data.get('salary_on_attendance')
    employee_add.over_time_applicable = request.data.get('over_time_applicable')
    employee_add.over_time_on = request.data.get('over_time_on')
    employee_add.mr_over_time_hours = request.data.get('mr_over_time_hours')
    employee_add.save()
        
    return Response('success')

@api_view(['GET'])
def BankEmpList(request):
    employeeGet = employee.objects.filter().order_by('bank_branch').distinct()
    employeeGet = connection.cursor()
    employeeGet.execute("SELECT DISTINCT bank_branch,ifsc FROM master_employee")

    employeeGet_RESULT = employeeGet.fetchall()
    tag = []
    for index in employeeGet_RESULT:
        tag.append({
            'bank_branch': index[0],
            'ifsc': index[1],
        })

    return Response(tag)

@api_view(['POST'])
def addemployeeBulk(request):
    DoublicateFound = []
    Count = 0;
    for index in request.data:
        # Selectie querry
        query = Q(contact_address_proof_aadhar_no = request.data[Count].get('contact_address_proof_aadhar_no'))
        query.add(Q(contact_address_proof_pan = request.data[Count].get('contact_address_proof_pan')), Q.OR)
        query.add(Q(work_man_no_int = request.data[Count].get('work_man_no_int')), Q.OR)
        query.add(Q(gate_pass_no = request.data[Count].get('gate_pass_no')), Q.OR)
        query.add(Q(safety_pass_no = request.data[Count].get('safety_pass_no')), Q.OR)
        query.add(Q(rfid_no = request.data[Count].get('rfid_no')), Q.OR)

        employeeCheckIF = employee.objects.filter(query)

        if employeeCheckIF:
            DoublicateFound.append({
                'employee_name': request.data[Count].get('employee_name'),
                'contact_address_proof_aadhar_no': request.data[Count].get('contact_address_proof_aadhar_no'),
                'contact_address_proof_pan': request.data[Count].get('contact_address_proof_pan'),
                'work_man_no_int': request.data[Count].get('work_man_no_int'),
                'gate_pass_no': request.data[Count].get('gate_pass_no'),
                'safety_pass_no': request.data[Count].get('safety_pass_no'),
            })
        else:
            employee_add = employee()
            employee_add.employee_name = request.data[Count].get('employee_name')
            employee_add.gender = request.data[Count].get('gender')
            employee_add.marital_status = request.data[Count].get('marital_status')
            employee_add.date_of_birth = request.data[Count].get('date_of_birth')
            employee_add.father_name = request.data[Count].get('father_name')
            employee_add.working_status = request.data[Count].get('working_status')
            employee_add.date_of_joining = request.data[Count].get('date_of_joining')
            employee_add.date_of_resigning = request.data[Count].get('date_of_resigning')

            employee_add.residential_address_line_one = request.data[Count].get('residential_address_line_one')
            employee_add.residential_address_line_two = request.data[Count].get('residential_address_line_two')
            employee_add.residential_area = request.data[Count].get('residential_area')
            employee_add.residential_landmark = request.data[Count].get('residential_landmark')
            employee_add.residential_post_office = request.data[Count].get('residential_post_office')
            employee_add.residential_police_station = request.data[Count].get('residential_police_station')
            employee_add.residential_city_village = request.data[Count].get('residential_city_village')
            employee_add.residential_district = request.data[Count].get('residential_district')
            employee_add.residential_state = request.data[Count].get('residential_state')
            employee_add.residential_country = request.data[Count].get('residential_country')
            employee_add.residential_pin_code = request.data[Count].get('residential_pin_code')
            
            employee_add.permanent_address_line_one = request.data[Count].get('permanent_address_line_one')
            employee_add.permanent_address_line_two = request.data[Count].get('permanent_address_line_two')
            employee_add.permanent_area = request.data[Count].get('permanent_area')
            employee_add.permanent_landmark = request.data[Count].get('permanent_landmark')
            employee_add.permanent_post_office = request.data[Count].get('permanent_post_office')
            employee_add.permanent_police_station = request.data[Count].get('permanent_police_station')
            employee_add.permanent_city_village = request.data[Count].get('permanent_city_village')
            employee_add.permanent_district = request.data[Count].get('permanent_district')
            employee_add.permanent_state = request.data[Count].get('permanent_state')
            employee_add.permanent_country = request.data[Count].get('permanent_country')
            employee_add.permanent_pin_code = request.data[Count].get('permanent_pin_code')

            employee_add.contact_address_proof_email = request.data[Count].get('contact_address_proof_email')
            employee_add.contact_address_proof_mobile_one = request.data[Count].get('contact_address_proof_mobile_one')
            employee_add.contact_address_proof_mobile_two = request.data[Count].get('contact_address_proof_mobile_two')
            employee_add.contact_address_proof_phone = request.data[Count].get('contact_address_proof_phone')
            employee_add.contact_address_proof_contact_person_name = request.data[Count].get('contact_address_proof_contact_person_name')
            employee_add.contact_address_proof_contact_person_no = request.data[Count].get('contact_address_proof_contact_person_no')
            employee_add.contact_address_proof_aadhar_no = request.data[Count].get('contact_address_proof_aadhar_no')
            employee_add.contact_address_proof_pan = request.data[Count].get('contact_address_proof_pan')

            employee_add.work_man_no_int = request.data[Count].get('work_man_no_int')
            employee_add.site = request.data[Count].get('site')
            employee_add.department = request.data[Count].get('department')
            employee_add.designation = request.data[Count].get('designation')
            employee_add.pf_applicable = request.data[Count].get('pf_applicable')
            employee_add.uan_p_f_no = request.data[Count].get('uan_p_f_no')
            employee_add.esic_applicable = request.data[Count].get('esic_applicable')
            employee_add.esic_no = request.data[Count].get('esic_no')
            employee_add.reverse_pf_esi = request.data[Count].get('reverse_pf_esi')
            employee_add.bonus_per_month = request.data[Count].get('bonus_per_month')

            employee_add.work_order_no = request.data[Count].get('work_order_no')
            employee_add.gate_pass_no = request.data[Count].get('gate_pass_no')
            employee_add.gate_pass_due_date = request.data[Count].get('gate_pass_due_date')
            employee_add.safety_pass_no = request.data[Count].get('safety_pass_no')
            employee_add.safety_pass_due_date = request.data[Count].get('safety_pass_due_date')
            employee_add.rfid_no = request.data[Count].get('rfid_no')
            employee_add.rfid_due_date = request.data[Count].get('rfid_due_date')

            employee_add.bank_name = request.data[Count].get('bank_name')
            employee_add.bank_branch = request.data[Count].get('bank_branch')
            employee_add.a_c_no = request.data[Count].get('a_c_no')
            employee_add.ifsc = request.data[Count].get('ifsc')
            employee_add.a_c_holder_name = request.data[Count].get('a_c_holder_name')

            employee_add.basic = request.data[Count].get('basic')
            employee_add.pay_rate = request.data[Count].get('pay_rate')
            employee_add.actual_rate = request.data[Count].get('actual_rate')
            employee_add.da = request.data[Count].get('da')
            employee_add.hra_float = request.data[Count].get('hra_float')
            employee_add.ca_float = request.data[Count].get('ca_float')
            employee_add.food_float = request.data[Count].get('food_float')
            employee_add.miscellaneous_float = request.data[Count].get('miscellaneous_float')
            employee_add.old_DA = request.data[Count].get('old_DA')
            employee_add.payment_mode = request.data[Count].get('payment_mode')
            employee_add.sunday_payable = request.data[Count].get('sunday_payable')
            employee_add.hra = request.data[Count].get('hra')
            employee_add.Food = request.data[Count].get('Food')
            employee_add.ca = request.data[Count].get('ca')
            employee_add.miscellaneous = request.data[Count].get('miscellaneous')
            employee_add.leave_days = request.data[Count].get('leave_days')
            employee_add.salary_on_attendance = request.data[Count].get('salary_on_attendance')
            employee_add.over_time_applicable = request.data[Count].get('over_time_applicable')
            employee_add.over_time_on = request.data[Count].get('over_time_on')
            employee_add.mr_over_time_hours = request.data[Count].get('mr_over_time_hours')
            employee_add.save()

        Count += 1;
        
    return Response(DoublicateFound)

@api_view(['GET','POST'])
def addUpdateOrListHoliday(request):
    if request.method == 'POST':
        Count = 0;
        holiday_list.objects.all().delete()
        for index in request.data:
            holiday_list_add = holiday_list()
            holiday_list_add.holiday_date = request.data[Count].get('holiday_date')
            holiday_list_add.holiday_type = request.data[Count].get('holiday_type')
            holiday_list_add.save()

            Count += 1;
            
        return Response('success')

    if request.method == 'GET':
        tag = []
        GetHolidayList = holiday_list.objects.filter()
        for index in GetHolidayList:
            tag.append({
                # 'id': index.id,
                'holiday_date': index.holiday_date,
                'holiday_type': index.holiday_type,
            })
        return Response(tag)


@api_view(['POST'])
def ListAttendance(request):
    tag = []
    Count = 0;
    for index in request.data:
        GetHolidayList = attendance_for_user.objects.filter(date= request.data[Count].get('date'),employee_id= request.data[Count].get('employee_id'))
        if GetHolidayList:
            employee_name = employee.objects.filter(id= GetHolidayList[0].employee_id)
            employee_name_get = 'N.A'
            if employee_name:
                employee_name_get = employee_name[0].employee_name
            tag.append({
                'id': GetHolidayList[0].id,
                'date': GetHolidayList[0].date,
                'employee_id': GetHolidayList[0].employee_id,
                'employee_name': employee_name_get,
                'attendance': GetHolidayList[0].attendance,
                'readvalue': False
            })
            Count += 1;
        else:
            tag.append({
                'id': Count,
                'date': request.data[Count].get('date'),
                'employee_id': request.data[Count].get('employee_id'),
                'employee_name': request.data[Count].get('employee_name'),
                'attendance': request.data[Count].get('attendance'),
                'readvalue': True
            })
            Count += 1;
    return Response(tag)

@api_view(['POST'])
def AddBulkAttendance(request):
    tag = []
    Count = 0
    CountTemp = 0
    exist = 0
    TotalWorkDays = 0

    Rate = 0
    TotalAmount = 0
    pf_deduction = 0
    esi_deduction = 0
    pf_amount = 0
    esi_amount = 0
    
    CounbtTotal = 0
    for index in request.data:
        CounbtTotal += 1 
        if request.data[CountTemp].get('attendance') == 'P' or request.data[CountTemp].get('attendance') == 'E' or request.data[CountTemp].get('attendance') == 'F':
            TotalWorkDays += 1
            employeeData = employee.objects.filter(id= request.data[int(CounbtTotal) - 1].get('employee_id'))
            Rate = employeeData[0].pay_rate
        CountTemp += 1;

    for index in request.data:
        GetHolidayList = attendance_for_user.objects.filter(date= request.data[Count].get('date'),employee_id= request.data[Count].get('employee_id'))
        if GetHolidayList:
            exist += 1
            Count += 1;
        else:
            if request.data[Count].get('attendance') == '':
                pass
            else:
                attendance_for_user_add = attendance_for_user()
                attendance_for_user_add.date = request.data[Count].get('date')
                attendance_for_user_add.employee_id = request.data[Count].get('employee_id')
                attendance_for_user_add.attendance = request.data[Count].get('attendance')
                attendance_for_user_add.save()


                # Change Date
                dateYearTemp = datetime.strptime(request.data[Count].get('date'), "%Y-%m-%d").date()
                dateYear = datetime.strftime(dateYearTemp, '%Y')
                dateMonth = datetime.strftime(dateYearTemp, '%m')

                # countAttendance = 0
                # countAttendance = attendance_for_user.objects.filter(date__month= dateMonth, date__year= dateYear,employee_id= request.data[Count].get('employee_id')).count()
                
                # payslip_per_user_Check = payslip_per_user.objects.filter(employee_id = request.data[Count].get('employee_id'), date__year = dateYear, date__month = dateMonth).exists()

                # count total work days
                
            Count += 1;
    print(TotalWorkDays)
    employeeData = employee.objects.filter(id= request.data[int(CounbtTotal) - 1].get('employee_id'))
    if request.data[int(CounbtTotal) - 1].get('attendance') != '':

        get_persent_get = get_persent.objects.get(id= 1)
        pf_deduction = get_persent_get.pf
        esi_deduction = get_persent_get.esi

        TotalAmount = float(Rate) * float(TotalWorkDays)
        pf_amount = (float(TotalAmount) * float(pf_deduction)) / 100
        esi_amount = (float(TotalAmount) * float(esi_deduction)) / 100

        # generate pay slip
        payslip_per_user_add = payslip_per_user()
        payslip_per_user_add.employee_id = employeeData[0].id
        payslip_per_user_add.total_working_day = TotalWorkDays
        payslip_per_user_add.date = request.data[int(CounbtTotal) - 1].get('date')
        payslip_per_user_add.rate = Rate
        payslip_per_user_add.total_amount = TotalAmount
        payslip_per_user_add.pf_deduction = pf_deduction
        payslip_per_user_add.pf_amount = pf_amount
        payslip_per_user_add.esi_deduction = esi_deduction
        payslip_per_user_add.esi_amount = esi_amount
        payslip_per_user_add.save()
        
    if exist == 0:
        return Response('success')
    else:
        return Response('exist')

@api_view(['POST'])
def SearchEmployee(request):
    tag = []
    # Selectie querry
    query = Q(id__icontains = request.data.get('dataSearch'))
    query.add(Q(employee_name__icontains = request.data.get('dataSearch')), Q.OR)
    query.add(Q(contact_address_proof_mobile_one__icontains = request.data.get('dataSearch')), Q.OR)
    query.add(Q(uan_p_f_no__icontains = request.data.get('dataSearch')), Q.OR)

    employeeCheckIF = employee.objects.filter(query)[0:4]

    # Get current data
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d")

    for index in employeeCheckIF:
        DepartmentName = 'N.A'
        DesignationName = 'N.A'
        SiteName = 'N.A'
        LastAttendance = 'N.A'

        LastDateAttendanse = attendance_for_user.objects.filter(employee_id= index.id, date__lte= current_time).order_by('-id')
        if LastDateAttendanse:
            LastAttendance = LastDateAttendanse[0].date

        if index.department == '':
            pass
        else:
            DepartmentData = department.objects.filter(id=index.department)
            if DepartmentData:
                DepartmentName = DepartmentData[0].name

        if index.designation == '':
            pass
        else:
            DesignationData = designation.objects.filter(id=index.designation)
            if DesignationData:
                DesignationName = DesignationData[0].name
        
        if index.site == '':
            pass
        else:
            siteData = site.objects.filter(id=index.site)
            if siteData:
                SiteName = siteData[0].name

        tag.append({
            'id': index.id,
            'employee_name': index.employee_name,
            'department': DepartmentName,
            'designation': DesignationName,
            'contact_address_proof_mobile_one': index.contact_address_proof_mobile_one,
            'uan_p_f_no': index.uan_p_f_no,
            'site': SiteName,
            'last_attendance': LastAttendance,
        })
    return Response(tag)

def GetMonthCheckList(month):
    if month == '01':
        return 'January'
    
    elif month == '02':
        return 'February'
    
    elif month == '03':
        return 'March'
    
    elif month == '04':
        return 'April'
    
    elif month == '05':
        return 'May'
    
    elif month == '06':
        return 'June'
    
    elif month == '07':
        return 'July'
    
    elif month == '08':
        return 'August'
    
    elif month == '09':
        return 'September'
    
    elif month == '10':
        return 'October'
    
    elif month == '11':
        return 'November'
    
    elif month == '12':
        return 'December'

@api_view(['POST'])
def GetPayslipSearchData(request):
    if request.data.get('employee_id') != '':
        employee_GET = employee.objects.filter(id= request.data.get('employee_id'))
    else:
        employee_GET = employee.objects.filter()
    tag = []
    for item in employee_GET:

        site_name = 'N.A'
        a_c_no = item.a_c_no
        ifsc = item.ifsc
        esic_no = item.esic_no

        site_get = site.objects.filter(id= item.site)
        if site_get:
            site_name = site_get[0].name
        
        payslip_per_user_GET = payslip_per_user.objects.filter(employee_id= item.id, date__year= request.data.get('years'), date__month= request.data.get('months'))

        Month = 'N.A'
        Temp = []
        TotalWorkingDays = 0
        Rate = 0
        TotalAmount = 0
        pf_deduction = 0
        esi_deduction = 0
        pf_amount = 0
        esi_amount = 0

        for index in payslip_per_user_GET:
            TotalWorkingDays += 1
            Rate = index.rate
            TotalAmount += float(index.total_amount)
            pf_deduction = index.pf_deduction
            esi_deduction = index.esi_deduction
            pf_amount += float(index.pf_amount)
            esi_amount += float(index.esi_amount)

        Month = GetMonthCheckList(request.data.get('months'))
        tag.append({
            'employee_name': item.employee_name,
            'month': Month,
            'year': request.data.get('years'),
            'total_working': TotalWorkingDays,
            'rate': Rate,
            'total_amount': TotalAmount,
            'pf_deduction': pf_deduction,
            'esi_deduction': esi_deduction,
            'pf_amount': pf_amount,
            'esi_amount': esi_amount,
            'site_name': site_name,
            'site_amount': 0,
            'gross_amount': TotalAmount + 0 ,
            'net_amount': ( TotalAmount + 0 ) - ( pf_amount + esi_amount ),
            'account_no': a_c_no,
            'ifsc_code': ifsc,
            'esi_account_no': esic_no,
        })
                
    
    return Response(tag)
