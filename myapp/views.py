from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Employees
from .forms import ModifyForm
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import leave
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Salary_slip
from .models import admins
from .models import attendance
from .forms import EmployeeForm


###############################################             SEARCH                          ###############################################

def search(request):
    if request.method == 'POST':
        ecode = request.POST['empsearch']
        search_details = Employees.objects.filter(Employee_Code=ecode)

      
        
    return render(request, "show_search.html", {'search_data': search_details})


##############################################               MODIFY                  ####################################################
def modify(request,employee_code):
    employee = get_object_or_404(Employees, Employee_Code=employee_code)

    if request.method == 'POST':
        form = ModifyForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            

    else:
        form = ModifyForm(instance=employee)

    return render(request, "modify.html", {'form': form, 'employee': employee})



###############################################             Attendance Search                          ###############################################
def attsearch(request):
     if request.method=="POST":
          code=request.POST['asearch']
          employees=attendance.objects.filter(Employee_Code=code)
     return render(request,"attendancesearch.html",{'employee':employees})

###########################################        LEAVE SEARCH          #################################################################

def leavesearch(request):
     if request.method=="POST":
          lsearch=request.POST['lsearch']
          employee=leave.objects.filter(Employee_Name=lsearch)

     return render(request,"leavesearch.html",{'employee':employee})


############################################               LEAVE                         ####################################################
def leavepage(request):
     if request.method=="POST":
          lname=request.POST['lename']
          lsdate=request.POST['leavesdate']
          ledate=request.POST['leaveedate']
          ltype=request.POST['ltype']
          lreason=request.POST['reason']
          obj=leave(Employee_Name=lname,Start_Date=lsdate,End_Date=ledate,Leave_Type=ltype,Reason=lreason)
          obj.save()
     return render(request,"leavepage.html")


##############################################           ATTENDANCE                       ################################################

def attendancepage(request):
    employees = Employees.objects.all()
    only_date = datetime.now().date()
    if request.method == "POST":
        for i in employees:
            attcode = request.POST.get(f'att_code_{i.pk}')
            attname = request.POST.get(f'att_name_{i.pk}')
            attdate = request.POST.get(f'att_date_{i.pk}')
            attstatus = request.POST.get(f'att_status_{i.pk}', '')
            
            a = attendance(Employee_Code=attcode, Employee_Name=attname, Date=attdate, status=attstatus)
            a.save()
    return render(request,'attendance.html',{'employees':employees,'datetoday':only_date})
     


###############################################         EMPLOYEE FILE                      ###############################################


def Employeefile(request):
    data=Employees.objects.all
    return render(request,'employee_file.html',{'data': data})


###############################################             NEW EMPLOYEE                  ###############################################


def new_employee(request):
    submitted=False
    if request.method=='POST':
         form=EmployeeForm(request.POST)
         if form.is_valid():
              form.save()

              return HttpResponseRedirect('/NewEmployee?submmitted=True')
    else:
         form=EmployeeForm
         if 'submitted' in request.GET:
              submitted=True
    return render(request,"new_employee.html",{'form':form,'submitted':submitted})


###############################################             LOGIN                       ###############################################


def login(request):
    if request.method == 'POST':
        user = request.POST.get('admin_name')
        password = request.POST.get('admin_pass')
        sel = request.POST.get('select_file')

        # Check if a user with the provided username and password exists
        user_exists = admins.objects.filter(username=user, password=password).exists()

        if user_exists :
            url = reverse('home')
            return HttpResponseRedirect(url)
        else:
             return render(request,"login.html")
        
             


    return render(request,"login.html")


###############################################             SALARY STATEMENT                         ###############################################


def salary_statement(request):
    employees = Employees.objects.all()
    salary_list = []

    for employee in employees:
        ecode=employee.Employee_Code
        ename=employee.Employee_Name
        des=employee.Employee_Role
        bsalary = employee.Employee_Bsalary
        calculated_da = bsalary * 55 / 100
        calculated_hra = bsalary * 35 / 100
        calculated_con = bsalary * 15 / 100
        calculated_gross = bsalary + calculated_hra + calculated_con + calculated_da
        calculated_ded = bsalary * 30 / 100
        calculated_net = calculated_gross - calculated_ded

        # Create a dictionary containing salary details for the current employee
        employee_salary = {
            'Employee_Code':ecode,
            'Employee_Name':ename,
            'Employee_Role':des,
            'Employee_Bsalary': bsalary,
            'Gross': calculated_gross,
            'deduction': calculated_ded,
            'net': calculated_net,
        }

        salary_list.append(employee_salary)

    return render(request, "salary_statement.html", {'salary_list': salary_list})


###############################################             SALARY SLIP                      ###############################################


def salary_slip(request):
    if request.method == 'POST':
        month = request.POST['select_month']
        year = request.POST['salary_year']
        code = request.POST['salary_ecode']
        daysw=request.POST['salary_daysw']
        employee = Employees.objects.filter(Employee_Code=code).first()
        if (month=="January" or month=="March" or month=="May" or month=="July" or month=="August" or month=="Octomber" or month=="December"):
                tdays=31
        elif(month=="Feburary" and year%4==0):
                tdays=29
        elif(month=="Feburary"):
                tdays=28
        else:
                tdays=30
        

        if employee:
            ename = employee.Employee_Name
            

            bsalary_str = employee.Employee_Bsalary
            bsalary = int(bsalary_str)
            salary_per_day=bsalary//int(tdays-4)
            asalary=salary_per_day*int(daysw)
            calculated_da = int(asalary* 55 / 100)
            calculated_hra = int(asalary* 35 / 100)
            calculated_con = int(asalary* 15 / 100)
            calculated_gross = int(asalary+ calculated_hra + calculated_con + calculated_da)
            calculated_ded = int(asalary*7 / 100)
            calculated_net = int(calculated_gross - calculated_ded)
        

    
    obj1=Salary_slip(month=month,year=year,Employee_Code=code,Employee_Name=ename,Employee_Bsalary=bsalary,No_Of_Days_Worked=daysw,Salary_of_Month=asalary,Da=calculated_da,Hra=calculated_hra,Conveyance=calculated_con,Gross=calculated_gross,Deduction=calculated_ded,Net=calculated_net)
    obj1.save()
    return render(request, "salary_slip.html", {
                'month': month,
                'year': year,
                'Employee_Name': ename,
                'Employee_Code': code,
                'basic': bsalary,
                'deduction':calculated_ded,
                'da': calculated_da,
                'hra': calculated_hra,
                'con': calculated_con,
                'grosspay': calculated_gross,
                'net': calculated_net,
            })
#####################################               MODIFIY CONFIRMED              ########################################################
def mod_confirmed(request):
    return render(request,"modified_confirmed.html")

###################################                  HOME                   ################################################################
def home(request):
     return render(request,"home.html")

#############################################         ABOUT US              ################################################################
def about(request):
     return render(request,"aboutus.html")

#############################################        MANAGE              ##################################################################
def manage(request):
     return render(request,"manage.html")

##############################################       CONTACT             ##################################################################
def contact(request):
     return render(request,"contact.html")