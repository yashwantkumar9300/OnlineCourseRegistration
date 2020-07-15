"""OCR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Admin part
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_login_check/',views.admin_login_check,name="admin_login_check"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('schedule_class/',views.schedule_class,name="schedule_class"),
    path('save_schedule/',views.save_schedule,name="save_schedule"),
    path('view_schedule_class/',views.view_schedule_class,name="view_schedule_class"),
    path('update_schedule/',views.update_schedule,name="update_schedule"),
    path('update_class/',views.update_class,name="update_class"),
    path('delete_schedule/',views.delete_schedule,name="delete_schedule"),
    path('view_student/',views.view_student,name="view_student"),
    # User Part
    path('',views.showIndex,name="main"),
    path('user_register/',views.user_register,name="user_register"),
    path('Student_save/',views.Student_save,name="Student_save"),
    path('student_login/',views.student_login,name="student_login"),
    path('student_login_check/',views.student_login_check,name="student_login_check"),
    path('Contact_page/',views.Contact_page,name="Contact_page"),
    path('student_home/',views.student_home,name="student_home"),
    path('enroll_course/',views.enroll_course,name="enroll_course"),
    path('save_enroll/',views.save_enroll,name="save_enroll"),
    path('view_enroll/',views.view_enroll,name="view_enroll"),
    path('cancel_enroll/',views.cancel_enroll,name="cancel_enroll"),
    path('delete_enroll/',views.delete_enroll,name="delete_enroll")
]
