from django.contrib import admin

from .models import Crud_Model, Dept_model, UserOTP

# Register your models here.
admin.site.register(Crud_Model)
admin.site.register(Dept_model)
admin.site.register(UserOTP)