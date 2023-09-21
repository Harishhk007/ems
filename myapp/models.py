from django.db import models

class Employees(models.Model):
    
    Employee_Name=models.CharField(max_length=100,null=False,blank=False)
    Employee_Code=models.AutoField(primary_key=True,auto_created=True)
    Employee_Gender=models.CharField(max_length=100,null=False,blank=False)
    Employee_Role=models.CharField(max_length=100,null=False,blank=False)
    Employee_Doj=models.DateField(max_length=100,null=False,blank=False)
    Employee_Bsalary=models.IntegerField(max_length=100,null=False,blank=False)
   
    Employee_Fname=models.CharField(max_length=100,null=False,blank=False)
    Employee_Dob=models.DateField(max_length=100,null=False,blank=False)
    Employee_Fphone=models.CharField(max_length=100,null=False,blank=False)
    Employee_Adhaar=models.IntegerField(max_length=100,null=False,blank=False)
    Employee_Address=models.CharField(max_length=100,null=False,blank=False)
    Employee_Phone=models.IntegerField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.Employee_Name
    
class attendance(models.Model):
    Employee_Code=models.IntegerField(null=False,blank=False)
    Employee_Name=models.CharField(max_length=100,null=False,blank=False)
    Date=models.CharField(max_length=100,null=False,blank=False)
    status=models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return f"{str(self.Employee_Code)}-{self.Employee_Name}-{str(self.Date)}"

class admins(models.Model):
    username=models.CharField(max_length=100,null=False,blank=False)
    password=models.CharField(max_length=200,null=False,blank=False)
    code=models.AutoField(primary_key=True,null=False,blank=False)

    def __str__(self):
        return self.username

class  leave(models.Model):
    Employee_Code=models.IntegerField(max_length=100,null=False,blank=False)
    Start_Date=models.DateField(null=False,blank=False)
    End_Date=models.DateField(null=False,blank=False)
    Leave_Type=models.CharField(max_length=100,null=False,blank=False)
    Reason=models.CharField(max_length=1000,null=False,blank=False)

    def __str__(self):
        return f"{self.Employee_Code} - {str(self.Start_Date)}"
 
class Salary_slip(models.Model):
    month=models.CharField(max_length=30,null=False,blank=False)
    year=models.IntegerField(null=False,blank=False)
    Employee_Code=models.IntegerField(null=False,blank=False)
    Employee_Name=models.CharField(max_length=100,null=False,blank=False)
    Employee_Bsalary=models.IntegerField(null=False,blank=False)
    No_Of_Days_Worked=models.IntegerField(null=False,blank=False)
    Salary_of_Month=models.IntegerField(null=False,blank=False)
    Da=models.IntegerField(null=False,blank=False)
    Hra=models.IntegerField(null=False,blank=False)
    Conveyance=models.IntegerField(null=False,blank=False)
    Gross=models.IntegerField(null=False,blank=False)
    Deduction=models.IntegerField(null=False,blank=False)
    Net=models.IntegerField(null=False,blank=False)

    def __str__(self):
        return f"{self.Employee_Name} - {self.month} - {self.year}"
