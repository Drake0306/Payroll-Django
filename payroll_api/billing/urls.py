"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from auth_user.views import login

# master views
from master.views import url_data, ListUmo,  addUmo,  updateUom, updateListUom, updateUomStatus, addSITE, ListSite, updateListSite, updateSite,Listdepartment,adddepartment,updateListdepartment,updatedepartment,Listdesignation,adddesignation,updateListdesignation,updatedesignation,bankList,addbank,updateListbank,updatebank,stateList,addstate,updateListstate,updatestate,employeeList,addemployee, PincodeList, BankEmpList, addemployeeBulk, addUpdateOrListHoliday, ListAttendance, AddBulkAttendance, SearchEmployee, GetPayslipSearchData


urlpatterns = [
    path('admin/', admin.site.urls),

    # user login
    path('api/log-in', login ,name="Login"),

    # list
    path('api/', url_data),


    # SITE
    path('api/siteList', ListSite, name="list site"),
    path('api/site-add', addSITE, name="add data" ),
    path('api/site-update-list/<int:id>', updateListSite, name="list update site"),
    path('api/site-update/<int:id>', updateSite, name="update site"),

    # DEPARTMENT
    path('api/departmentList', Listdepartment, name="list department"),
    path('api/department-add', adddepartment, name="add data" ),
    path('api/department-update-list/<int:id>', updateListdepartment, name="list update department"),
    path('api/department-update/<int:id>', updatedepartment, name="update department"),
    
    # designation
    path('api/designationList', Listdesignation, name="list designation"),
    path('api/designation-add', adddesignation, name="add data" ),
    path('api/designation-update-list/<int:id>', updateListdesignation, name="list update designation"),
    path('api/designation-update/<int:id>', updatedesignation, name="update designation"),
    
    #PincodeList
    path('api/pin/list', PincodeList, name="pin code"),
    
    #bank
    path('api/bankList', bankList, name="bank list"),
    path('api/bank-add', addbank, name="add bank data"),
    path('api/bank-update-list/<int:id>', updateListbank, name="fetch data"),
    path('api/bank-update/<int:id>', updatebank, name="update data"),

    #state
    path('api/stateList', stateList, name="state list"),
    path('api/state-add', addstate, name="add state data"),
    path('api/state-update-list/<int:id>', updateListstate, name="fetch data"),
    path('api/state-update/<int:id>', updatestate, name="update data"),

    # employee
    path('api/employeeList', employeeList, name="employee list"),
    path('api/employee-add', addemployee, name="add employee data"),
    path('api/employee-bank-list', BankEmpList, name="employee-bank-list"),
    path('api/employee-add-bulk', addemployeeBulk, name="employee-bank-list"),
    
    #Holiday
    path('api/holiday/multi/url', addUpdateOrListHoliday, name="employee-bank-list"),
    
    #Attendance
    path('api/attendance/get/url', ListAttendance, name="attendance"),
    path('api/attendance/bulk/url/add', AddBulkAttendance, name="attendance"),
    path('api/attendance/employee/search/', SearchEmployee, name="attendance"),

    # Payslip
    path('api/pay/slip/search/', GetPayslipSearchData, name="attendance"),
]

 