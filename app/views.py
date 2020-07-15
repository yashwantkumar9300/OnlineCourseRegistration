
from django.shortcuts import render, redirect
from app.models import CourseModel,StudentModel,EnrollCourse
from django.contrib import messages
from django.db.utils import IntegrityError

# Admin Part
def admin_login(request):
    return render(request,"admin_login.html")

def admin_login_check(request):
    un = request.POST.get("t1")
    pas = request.POST.get("t2")
    if un == "yash" and pas == "kumar":
        return render(request,"admin_home.html")
    else:
        return render(request,"admin_login.html",{"error":"Invalid Username or Password"})

def admin_home(request):
    return render(request,"admin_home.html")

def schedule_class(request):
    return render(request,"schedule_class.html")

def save_schedule(request):
    cn = request.POST.get("t1")
    fn = request.POST.get("t2")
    dt = request.POST.get("t3")
    tm = request.POST.get("t4")
    fee = request.POST.get("t5")
    dur = request.POST.get("t6")
    CourseModel(cname=cn,fname=fn,date=dt,time=tm,fees=fee,duration=dur).save()
    messages.success(request, "Class Schedule is Done")
    return redirect('schedule_class')

def view_schedule_class(request):
    res = CourseModel.objects.all()
    return render(request,"view_schedule_class.html",{"data":res})

def update_schedule(request):
    id = request.GET.get("no")
    res = CourseModel.objects.get(idno=id)
    return render(request,"update_schedule.html",{"data":res})

def update_class(request):
    id = request.POST.get("t1")
    cn = request.POST.get("t2")
    fn = request.POST.get("t3")
    dt = request.POST.get("t4")
    tm = request.POST.get("t5")
    fee = request.POST.get("t6")
    dur = request.POST.get("t7")
    CourseModel.objects.filter(idno=id).update(cname=cn,fname=fn,date=dt,time=tm,fees=fee,duration=dur)
    messages.success(request, "Class Schedule is Update")
    return redirect('view_schedule_class')

def delete_schedule(request):
    id = request.GET.get("no")
    CourseModel.objects.filter(idno=id).delete()
    messages.success(request, "Class Schedule is Delete")
    return redirect('view_schedule_class')

def view_student(request):
    res = StudentModel.objects.all()
    return render(request,"view_student.html",{"data":res})

# User Part
def showIndex(request):
    res = CourseModel.objects.all()
    return render(request,"index.html",{"data":res})

def user_register(request):
    return render(request,"user_register.html")

def Student_save(request):
    sn = request.POST.get("t1")
    gen = request.POST.get("t2")
    con = request.POST.get("t3")
    em = request.POST.get("t4")
    pas = request.POST.get("t5")
    try:
        StudentModel(sname=sn,gender=gen,contact=con,email=em,password=pas).save()
        messages.success(request, "Registered Successfully !!!")
        return redirect('user_register')
    except IntegrityError:
        messages.success(request, "Student Already Registered !!!")
        return redirect('user_register')

def student_login(request):
    return render(request,"student_login.html")

def Contact_page(request):
    return render(request,"Contact_page.html")

res=""
def student_login_check(request):
    un = request.POST.get("t1")
    pas = request.POST.get("t2")
    try:
        global res
        res = StudentModel.objects.get(email=un,password=pas)
        return render(request,"student_home.html",{"data":res})
    except StudentModel.DoesNotExist:
        messages.success(request, "Invalid Username or Password !!!")
        return redirect('student_login')

def student_home(request):
    return render(request,"student_home.html",{"data":res})

def enroll_course(request):
    result = CourseModel.objects.all()
    return render(request,"enroll_course.html",{"info":result,"data":res})

def save_enroll(request):
    cn = request.POST.get("t1")
    fn = request.POST.get("t2")
    tm = request.POST.get("t3")
    fee = request.POST.get("t4")
    dur = request.POST.get("t5")
    sid = request.POST.get("t6")
    EnrollCourse(cname=cn, fname=fn, time=tm, fees=fee, duration=dur,sid=sid).save()
    messages.success(request, "Enrolled Successfully")
    return redirect('enroll_course')

def view_enroll(request):
    id = request.GET.get("no")
    ressult = EnrollCourse.objects.filter(sid=id)
    return render(request,"view_enroll.html",{"enroll":ressult,"data":res})

def cancel_enroll(request):
    id = request.GET.get("no")
    ressult = EnrollCourse.objects.filter(sid=id)
    return render(request, "cancel_enroll.html", {"enroll": ressult, "data": res})

def delete_enroll(request):
    id = request.GET.get("no")
    EnrollCourse.objects.filter(idno=id).delete()
    messages.success(request, "Enrolled is Cancel")
    return redirect('cancel_enroll')