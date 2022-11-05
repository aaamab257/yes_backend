from __future__ import division
from django.contrib import admin
from .models import Student
# Register your models here.


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id','name' ,'is_active', 'is_admin' , 'division')
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name' ,'state' ,'division','phone_number' , 'school',)}),
        ('Permissions', {'fields': ('is_admin','is_active')}),
    )
    search_fields = ('phone_number',)


admin.site.register(Student,StudentsAdmin)