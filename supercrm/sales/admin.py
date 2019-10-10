from django.contrib import admin
from sales import models
# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['username','password','email','telephone','is_active']
    list_editable = ['password','email','telephone',]

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','name','status','consultant']
    list_editable = ['status','consultant',]


admin.site.register(models.Customer,CustomerAdmin)
admin.site.register(models.ClassList)
admin.site.register(models.UserInfo,UserInfoAdmin)
admin.site.register(models.Campuses)
admin.site.register(models.ConsultRecord)
admin.site.register(models.Enrollment)
admin.site.register(models.CourseRecord)
admin.site.register(models.StudyRecord)
admin.site.register(models.Department)


