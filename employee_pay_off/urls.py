
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newEmployee/',views.new_employee,name="newemployee"),
    path('login/',views.login,name="login"),
    path('employeefiles/',views.Employeefile,name="employeefile"),
    path('salaryslip/',views.salary_slip,name="MonthlyPayFile"),
    path('modify/<int:employee_code>/', views.modify, name='modify'),
    path('salarystatement/',views.salary_statement,name="salarystatement"),
    path('employeedata/',views.search,name="searchpage"),
    path('modifyconfirmed/',views.mod_confirmed,name="mod_con"),
    path('home/',views.home,name="home"),
    path('about/',views.about,name="aboutus"),
    path('management/',views.manage,name="manage"),
    path('contact/',views.contact,name="contact"),
    path('attendance/',views.attendancepage,name="attendance"),
    path('leave/',views.leavepage,name="leave"),
    path('leavesearch/',views.leavesearch,name="leavesearch"),
    path('searchattendance/',views.attsearch,name="attsearch"),





    path('ehome/',views.employeehome,name="ehome"),
    path('Attendance/',views.employeeattendance,name="eattendance"),
    path('Attendancerecord/',views.eattsearch,name="eattsearch"),
    path('Salarystatements/',views.epayroll,name="SalaryStatements"),
    path('salarysearch/',views.salsearch,name="salsearch"),
    path('employeeinfo/',views.employeemanage,name="employeemanage"),
    path('employeeleave/',views.employeeleave,name="eleave"),
    path('employeeleaverecords/',views.employeeleavesearch,name="eleavesearch"),
    path('Aboutus/',views.employeeaboutus,name="employee_aboutus"),
    path('Contact/',views.employeecontact,name="employee_contact"),
    path('Changepass/<int:employee_code>/',views.changepass,name="changepass")
]
