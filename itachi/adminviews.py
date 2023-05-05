from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Course,Session_Year,CustomUser,Student,Faculty,Subject,Attendance,Attendance_Report,StudentApplication
from django.contrib import messages

import pandas as pd




@login_required(login_url='/')
def adminhome(request):
    student_count=Student.objects.all().count()
    course_count=Course.objects.all().count()
    faculty_count=Faculty.objects.all().count()
    subject_count=Subject.objects.all().count()
    
    context={
        'student_count':student_count,
        'course_count':course_count,
        'faculty_count':faculty_count,
        'subject_count':subject_count,
        
    }
    
    return render(request,'Adminy/adminhome.html',context)

@login_required(login_url='/')
def addstudent(request):
    course=Course.objects.all()
    session_year=Session_Year.objects.all()
    
    if request.method == "POST":
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        password=request.POST.get('password')
        course_id=request.POST.get('course_id')
        session_year_id=request.POST.get('session_year_id')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is already taken !')
            return redirect('addstudent')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username is already taken !')
            return redirect('addstudent')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type='3'
                
            )
            user.set_password(password)
            user.save()

            course=Course.objects.get(id=course_id)
            session_year=Session_Year.objects.get(id=session_year_id)
            
            student=Student(
                admin=user,
                address=address,
                session_year_id=session_year,
                course_id=course,
                gender=gender,
            )
            student.save()
            messages.success(request, user.first_name + " " + user.last_name + " is Succesfully Added as a Student")
            return redirect('addstudent')

            
        
    context={
        'course':course,
        'session_year':session_year,
    }
    
    return render(request,'Adminy/addstudent.html',context)

@login_required(login_url='/')
def viewstudent(request):
    
    student=Student.objects.all()
    
    context={
        'student':student,
    }
    return render(request,'Adminy/viewstudent.html',context)

@login_required(login_url='/')
def editstudent(request,id):
    student=Student.objects.filter(id=id)
    course=Course.objects.all()
    session_year=Session_Year.objects.all()
    context={
        'student':student,
        'course':course,
        'session_year':session_year,
    }
    return render(request,'Adminy/editstudent.html',context)

@login_required(login_url='/')
def updatestudent(request):
    
    if request.method == "POST":
        
        student_id=request.POST.get('student_id')
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        password=request.POST.get('password')
        course_id=request.POST.get('course_id')
        session_year_id=request.POST.get('session_year_id')
        
        user=CustomUser.objects.get(id=student_id)
        
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.username=username
        
        
        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic=profile_pic
        user.save()
        
        student = Student.objects.get(admin=student_id)
        student.address=address
        student.gender=gender
        
        course=Course.objects.get(id=course_id)
        student.course_id=course
        
        session_year=Session_Year.objects.get(id=session_year_id)
        student.session_year_id=session_year
        
        student.save()
        messages.success(request,'Records are succesfully updated !')
        return redirect('viewstudent')
        
    return render(request,'Adminy/editstudent.html',)

@login_required(login_url='/')
def deletestudent(request,admin):
    student=CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request,'Records are successfully deleted ! ')
    return redirect('viewstudent')

@login_required(login_url='/')
def addcourse(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        course=Course(
            name=course_name,
        )
        course.save()
        messages.success(request,'Course is Successfully Added !')
        return redirect('addcourse')
    return render(request,'Adminy/addcourse.html')

@login_required(login_url='/')
def viewcourse(request):
    
    course=Course.objects.all()
    context={
        'course':course,
    }
    return render(request,'Adminy/viewcourse.html',context)

@login_required(login_url='/')
def editcourse(request,id):
    course=Course.objects.get(id=id)
    context={
        'course':course,
    }
    return render(request,'Adminy/editcourse.html',context)

@login_required(login_url='/')
def updatecourse(request):
    if request.method == "POST":
        name=request.POST.get('name')
        course_id=request.POST.get('course_id')

        course=Course.objects.get(id=course_id)
        course.name=name
        course.save()
        messages.success(request,'Course is successfully updated !')
        return redirect('viewcourse')

    return render(request,'Adminy/editcourse.html')

@login_required(login_url='/')
def deletecourse(request,id):
    course=Course.objects.get(id=id)
    course.delete()
    messages.success(request,'Records are successfully deleted ! ')
    return redirect('viewcourse')

@login_required(login_url='/')
def addfaculty(request):
    if request.method == "POST":
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        password=request.POST.get('password')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is already taken !')
            return redirect('addfaculty')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username is already taken !')
            return redirect('addfaculty')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type='2'
                
            )
            
            user.set_password(password)
            user.save()
            faculty=Faculty(
                admin=user,
                address=address,
                gender=gender,
            )
            faculty.save()
            messages.success(request, user.first_name + " " + user.last_name + " is Succesfully Added as a Faculty")
            return redirect('addfaculty')
    return render(request,'Adminy/addfaculty.html')

@login_required(login_url='/')
def viewfaculty(request):
    
    faculty=Faculty.objects.all()
    
    context={
        'faculty':faculty,
    }
    return render(request,'Adminy/viewfaculty.html',context)

@login_required(login_url='/')
def editfaculty(request,id):
    faculty=Faculty.objects.filter(id=id)
    
    context={
        'faculty':faculty
        
    }
    return render(request,'Adminy/editfaculty.html',context)

@login_required(login_url='/')
def updatefaculty(request):
    
    if request.method == "POST":
        
        faculty_id=request.POST.get('faculty_id')
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        password=request.POST.get('password')
        
        
        user=CustomUser.objects.get(id=faculty_id)
        
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.username=username
        
        
        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic=profile_pic
        user.save()
        
        faculty = Faculty.objects.get(admin=faculty_id)
        faculty.address=address
        faculty.gender=gender
        
        
        
        faculty.save()
        messages.success(request,'Records are succesfully updated !')
        return redirect('viewfaculty')
        
    return render(request,'Adminy/editfaculty.html',)

@login_required(login_url='/')
def deletefaculty(request,admin):
    faculty=CustomUser.objects.get(id=admin)
    faculty.delete()
    messages.success(request,'Records are successfully deleted ! ')
    return redirect('viewfaculty')

@login_required(login_url='/')
def addsubject(request):
    course=Course.objects.all()
    faculty=Faculty.objects.all()

    if request.method == "POST":
        subject_name=request.POST.get('subject_name')
        course_id=request.POST.get('course_id')
        faculty_id=request.POST.get('faculty_id')
        
        course=Course.objects.get(id=course_id)
        faculty=Faculty.objects.get(id=faculty_id)
        
        subject=Subject(
            name=subject_name,
            course=course,
            faculty=faculty,
        )
        subject.save()
        messages.success(request,'Subject is successfully added !')
        return redirect('addsubject')
        
    context={
        'course':course,
        'faculty':faculty,
    }
    return render(request,'Adminy/addsubject.html',context)

@login_required(login_url='/')
def viewsubject(request):
    
    subject=Subject.objects.all()
    
    context={
        'subject':subject,
    }
    return render(request,'Adminy/viewsubject.html',context)


@login_required(login_url='/')
def editsubject(request,id):
    subject=Subject.objects.get(id=id)
    course=Course.objects.all()
    faculty=Faculty.objects.all()
    context={
        'subject':subject,
        'course':course,
        'faculty':faculty,
    }
    return render(request,'Adminy/editsubject.html',context)

@login_required(login_url='/')
def updatesubject(request):
    if request.method == "POST":
        name=request.POST.get('name')
        subject_id=request.POST.get('subject_id')
        subject_name=request.POST.get('subject_name')
        course_id=request.POST.get('course_id')
        faculty_id=request.POST.get('faculty_id')
        
        course=Course.objects.get(id=course_id)
        faculty=Faculty.objects.get(id=faculty_id)
        
        subject=Subject(
            id=subject_id,
            name=subject_name,
            course=course,
            faculty=faculty,
            
        )
        subject.save()
        messages.success(request,'Subject is successfully updated !')
        return redirect('viewsubject')

    return render(request,'Adminy/editsubject.html')

@login_required(login_url='/')
def deletesubject(request,id):
    subject=Subject.objects.get(id=id)
    subject.delete()
    messages.success(request,'Records are successfully deleted ! ')
    return redirect('viewsubject')


@login_required(login_url='/')
def addsession(request):
    if request.method == "POST":
        session_year_start=request.POST.get('session_year_start')
        session_year_end=request.POST.get('session_year_end')
        
        
        session=Session_Year(
            session_start=session_year_start,
            session_end=session_year_end,
        )
        session.save()
        messages.success(request,'Session is successfully added !')
        return redirect('addsession')
  
    return render(request,'Adminy/addsession.html')

@login_required(login_url='/')
def viewsession(request):
    
    session=Session_Year.objects.all()
    
    context={
        'session':session,
    }
    return render(request,'Adminy/viewsession.html',context)


@login_required(login_url='/')
def editsession(request,id):
    session=Session_Year.objects.filter(id=id)
    
    
    context={
        'session':session,
    }
    return render(request,'Adminy/editsession.html',context)

@login_required(login_url='/')
def updatesession(request):
    if request.method =="POST":
        session_id=request.POST.get('session_id')
        session_year_start=request.POST.get('session_year_start')
        session_year_end=request.POST.get('session_year_end')
        session=Session_Year(
            id=session_id,
            session_start=session_year_start,
            session_end=session_year_end,
        )
        session.save()
        
        messages.success(request,'Session is successfully updated !')
        return redirect('viewsession')

    return render(request,'Adminy/editsession.html')

@login_required(login_url='/')
def deletesession(request,id):
    session=Session_Year.objects.get(id=id)
    session.delete()
    messages.success(request,'Records are successfully deleted ! ')
    return redirect('viewsession')

@login_required(login_url='/')
def adminviewattendance(request):
    

    subject=Subject.objects.all()
    session_year=Session_Year.objects.all()
    action=request.GET.get('action')
    get_subject=None
    get_session_year=None
    attendance_date=None
    attendance_report=None
    if action is not None:
        if request.method == "POST":
            subject_id=request.POST.get('subject_id')
            session_year_id=request.POST.get('session_year_id')
            attendance_date=request.POST.get('attendance_date')

            get_subject=Subject.objects.get(id=subject_id)
            get_session_year=Session_Year.objects.get(id=session_year_id)
            attendance=Attendance.objects.filter(subject_id=get_subject,attendance_date=attendance_date)
            for i in attendance:
                attendance_id=i.id
                attendance_report=Attendance_Report.objects.filter(attendance_id=attendance_id,)
                

    
    context={
        'subject':subject,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'attendance_date':attendance_date,
        'attendance_report':attendance_report,
    }
    return render(request,'Adminy/adminviewattendance.html',context)

@login_required(login_url='/')
def viewapplication(request):
    student_application=StudentApplication.objects.all()
    context={
        'student_application':student_application
    }
    return render(request,'Adminy/viewapplication.html',context)

@login_required(login_url='/')
def approveapplication(request,id):
    appl = StudentApplication.objects.get(id=id)
    appl.status = 1
    appl.save()
    return redirect('viewapplication')

@login_required(login_url='/')
def declineapplication(request,id):
    appl = StudentApplication.objects.get(id=id)
    appl.status = 2
    appl.save()
    return redirect('viewapplication')

