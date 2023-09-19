from django import forms
from django.forms import ModelForm
from .models import Employees

class EmployeeForm(ModelForm):
    class Meta:
    
        model=Employees
        fields=('Employee_Name','Employee_Gender','Employee_Role','Employee_Doj','Employee_Bsalary','Employee_Fname','Employee_Dob','Employee_Fphone','Employee_Adhaar','Employee_Address','Employee_Phone')
        labels={'Employee_Name':'Employee Name',
                'Employee_Gender':'Employee Gender',
                'Employee_Role':'Employee Role',
                'Employee_Doj':'Date of Joining',
                'Employee_Bsalary':'Employee Basic Salary',
                'Employee_Fname':'Employee Father\'s \ Husband\'s Name ',
                'Employee_Dob':'Employee Date of Birth',
                'Employee_Fphone':'Employee Care of Phone Number',
                'Employee_Adhaar':'Employee Adhaar Number',
                'Employee_Address':'Employee Address',
                'Employee_Phone':'Employee Phone'}


        GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ]
        ROLE_CHOICES = [
        ('Teacher', 'TEACHER'),
        ('Office Staff', 'OFFICE STAFF'),
        ('Security', 'SECURITY'),
        ('House Keeper', 'HOUSE KEEPER'),
        ]

        widgets={
            'Employee_Name': forms.TextInput(attrs={'class':'form-control','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px;text-align:center','placeholder':'Enter Name'}),
            'Employee_Gender': forms.Select(attrs={'class':'form-control','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:20px;text-align:center' }, choices=GENDER_CHOICES),
            'Employee_Role':forms.Select(attrs={'class':'form-control','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:20px;text-align:center'}, choices=ROLE_CHOICES),
            'Employee_Doj':forms.DateInput(attrs={'class':'form-control','type':'date','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px'}),
            'Employee_Bsalary':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Basic Salary','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px'}),
            'Employee_Fname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Father / Husband Name','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px'}),
            'Employee_Dob':forms.DateInput(attrs={'class':'form-control','type':'date','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px'}),
            'Employee_Fphone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Careof\'s phone Number ','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px'}),
            'Employee_Adhaar':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Adhaar Number','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px'}),
            'Employee_Address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px'}),
            'Employee_Phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Phone Number','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px'}),

        }



class ModifyForm(ModelForm):
    class Meta:
    
        model=Employees
        fields=('Employee_Gender','Employee_Role','Employee_Doj','Employee_Bsalary','Employee_Fname','Employee_Dob','Employee_Fphone','Employee_Adhaar','Employee_Address','Employee_Phone')
        labels={
                'Employee_Gender':'Employee Gender',
                'Employee_Role':'Employee Role',
                'Employee_Doj':'Date of Joining',
                'Employee_Bsalary':'Employee Basic Salary',
                'Employee_Fname':'Employee Father\'s \ Husband\'s Name ',
                'Employee_Dob':'Employee Date of Birth',
                'Employee_Fphone':'Employee Care of Phone Number',
                'Employee_Adhaar':'Employee Adhaar Number',
                'Employee_Address':'Employee Address',
                'Employee_Phone':'Employee Phone'}


        GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ]
        ROLE_CHOICES = [
        ('Teacher', 'TEACHER'),
        ('Office Staff', 'OFFICE STAFF'),
        ('Security', 'SECURITY'),
        ('House Keeper', 'HOUSE KEEPER'),
        ]

        widgets={
            
            'Employee_Gender': forms.Select(attrs={'class':'form-control','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:20px;text-align:center' }, choices=GENDER_CHOICES),
            'Employee_Role':forms.Select(attrs={'class':'form-control','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:20px;text-align:center'}, choices=ROLE_CHOICES),
            'Employee_Doj':forms.DateInput(attrs={'class':'form-control','type':'date','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px'}),
            'Employee_Bsalary':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Basic Salary','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px'}),
            'Employee_Fname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Father / Husband Name','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px'}),
            'Employee_Dob':forms.DateInput(attrs={'class':'form-control','type':'date','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px'}),
            'Employee_Fphone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Careof\'s phone Number ','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px'}),
            'Employee_Adhaar':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Adhaar Number','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px'}),
            'Employee_Address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px'}),
            'Employee_Phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Phone Number','style':'width:500px;background-color:transparent;color:white;font-family:"poppins";font-size:25px'}),

        }
        

    