from django.urls import path

from .views import hello_view, add_view, edit_view, delete_view, add_dept_view, edit_dept_view, delete_dept_view, \
    signup_view, login_view, forget_password_views, otp_verify_views, reset_password_views

urlpatterns = [
    path("hello/",hello_view,name='hello'),
    path("hello/add",add_view,name='add'),
    path("hello/edit/<int:e_id>",edit_view,name='edit'),
    path("hello/delete/<int:d_id>",delete_view,name='delete'),
    path("hello/add/dept", add_dept_view, name='add_dept'),
    path("hello/edit/dept/<int:ed_id>", edit_dept_view, name='edit_dept'),
    path("hello/delete/dept/<int:dd_id>", delete_dept_view, name='delete_dept'),

    path("signup/", signup_view, name='signup'),
    path("login/", login_view, name='login'),
    path("forget-password/", forget_password_views, name='forget-password'),
    path("otp-verify/", otp_verify_views, name='otp-verify'),
    path("reset-password/", reset_password_views, name='reset-password'),

]
