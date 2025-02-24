
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from .models import Crud_Model, Dept_model


# Create your views here.
def hello_view(request):
    template_name = 'index.html'
    employee_obj = Crud_Model.objects.all()
    dept_obj = Dept_model.objects.all()

    search_name = request.GET.get("search_first_name","")
    if search_name:
        employee_obj = employee_obj.filter(Q(first_name__icontains = search_name),Q(last_name__icontains = search_name))
    print(search_name)

    context = {
        "employee_obj":employee_obj,
        "dept_obj":dept_obj,
        "search_name":search_name
   }
    return render(request,template_name,context)

def add_view(request):
    template_name = 'add.html'
    employee_obj = Crud_Model.objects.all()
    dept_obj = Dept_model.objects.all()
    context = {"employee_obj":employee_obj,"dept_obj":dept_obj}

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        doj = request.POST['doj']
        dept_id = request.POST["dept"]


        if employee_obj.filter(email=email).exists():
            context["error"] = "Email All Ready Exists"
            return render(request, template_name, context)

        employee_obj = Crud_Model(
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone = phone,
            doj = doj,
            dept_id = dept_id
        )
        employee_obj.save()

        return redirect("/hello/")
    return render(request, template_name, context)

def edit_view(request,e_id):
    template_name = 'add.html'
    employee_obj = Crud_Model.objects.get(id = e_id)
    dept_obj = Dept_model.objects.all()
    print(employee_obj)

    context = {"employee_obj":employee_obj,"dept_obj":dept_obj}

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        doj = request.POST['doj']
        dept_id = request.POST["dept"]

        employee_obj.first_name = first_name
        employee_obj.last_name = last_name
        employee_obj.email = email
        employee_obj.phone = phone
        employee_obj.doj = doj
        employee_obj.dept_id = dept_id
        employee_obj.save()

        return redirect("/hello/")
    return render(request, template_name, context)

def delete_view(request,d_id):
    employee_obj = Crud_Model.objects.get(id = d_id)
    print(employee_obj)
    employee_obj.delete()
    return redirect("/hello/")

def add_dept_view(request):
    template_name = 'add_dept.html'
    context = {}
    if request.method == "POST":
        name = request.POST["name"]

        dept_obj = Dept_model(name = name)
        dept_obj.save()
        return redirect("/hello/")
    return render(request, template_name, context)

def edit_dept_view(request,ed_id):
    template_name = 'add_dept.html'
    dept_obj = Dept_model.objects.get(id = ed_id)
    print(dept_obj)
    context = {"dept_obj": dept_obj}
    if request.method == "POST":
        name = request.POST['name']

        dept_obj.name = name
        dept_obj.save()

        return redirect("/hello/")

    return render(request, template_name, context)

def delete_dept_view(request,dd_id):
    dept_obj = Dept_model.objects.get(id = dd_id)
    dept_obj.delete()
    return redirect("/hello/")

def signup_view(request):
    template_file = "signup.html"
    context = {}
    if request.method == "POST":
        first_name =request.POST["first_name"]
        last_name =request.POST["last_name"]
        email =request.POST["email"]
        username = email
        password =request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already registered.")
            return render(request, "signup.html", context)

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, "signup.html")

        user = User.objects.create_user(username,email,password)
        user.first_name  = first_name
        user.last_name  = last_name
        user.save()
        return redirect("login")
    return render(request,template_file,context)

def login_view(request):
    template_name = "login.html"
    context = {}
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user_obj = User.objects.filter(email=email).first()
        if user_obj:
            user = authenticate(request,username=user_obj.username,password=password)
            if user is not None:
                login(request, user)
                next_param = request.GET.get("next", settings.LOGOUT_REDIRECT_URL)
                return redirect(next_param)
            else:
                messages.error(request, "email and password is incorrect")
        else:
            messages.error(request, "User is not registered.")
    return render(request, template_name, context)

def forget_password_views(request):
    template_name = "forget-password.html"
    context = {}
    if request.method == "POST":
        email = request.POST["email"]
        user = User.objects.filter(email=email).exists()
        print(user)
        if user:
            return redirect(f"/otp-verify?email={email}")
        else:
            messages.error(request,"Email not found. Please enter a registered email.")
    return render(request, template_name, context)

def otp_verify_views(request):
    template_name = "otp-verify.html"
    context = {}
    if request.method == "POST":
        first = request.POST.get("first")
        second = request.POST.get("second")
        third = request.POST.get("third")
        fourth = request.POST.get("fourth")
        fifth = request.POST.get("fifth")
        sixth = request.POST.get("sixth")

        entered_otp = f"{first}{second}{third}{fourth}{fifth}{sixth}"
        if entered_otp == "123456":
            return redirect("/reset-password")
        else:
            messages.error(request,"Invalid OTP. Please try again.")


        print(entered_otp)
    return render(request, template_name, context)

def reset_password_views(request):
    template_name = "reset-password.html"
    context = {}
    return render(request, template_name, context)
