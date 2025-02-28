from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Dept_model(models.Model):
    name = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name},{self.created_at},{self.updated_at}"

class Crud_Model(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.BigIntegerField(null=True, default=None)
    doj = models.DateField(null=True, default=None)

    dept = models.ForeignKey(Dept_model,null=True,on_delete=models.SET_NULL,related_name="dept")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.email},{self.phone},{self.doj},{self.created_at},{self.updated_at}"

class UserOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user},{self.otp}"