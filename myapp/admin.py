from django.contrib import admin
from .models import Employees
from .models import Salary_slip
from .models import admins
from .models import attendance
from .models import leave

@admin.register(leave)
class leave(admin.ModelAdmin):
    pass

# Register your models here.
@admin.register(Employees)
class Employees(admin.ModelAdmin):
    pass

@admin.register(attendance)
class attendance(admin.ModelAdmin):
    pass

@admin.register(admins)
class admins(admin.ModelAdmin):
    pass


@admin.register(Salary_slip)
class Salary_slip(admin.ModelAdmin):
    pass
