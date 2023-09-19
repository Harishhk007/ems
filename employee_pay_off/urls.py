
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('NewEmployee/',views.new_employee,name="newemployee"),
    path('',views.login),
    path('Employeefiles/',views.Employeefile,name="employeefile"),
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
    path('searchattendance/',views.attsearch,name="attsearch")
]
