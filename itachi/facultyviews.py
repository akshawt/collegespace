from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Course,Session_Year,CustomUser,Student,Faculty,Subject,Attendance,Attendance_Report,StudentResult
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def facultyhome(request):
    return render(request,'Faculty/facultyhome.html')

@login_required(login_url='/')
def takeattendance(request):
    faculty_id=Faculty.objects.get(admin=request.user.id)
    subject=Subject.objects.filter(faculty=faculty_id)
    sessiom_year=Session_Year.objects.all()
    action=request.GET.get('action')

    get_subject=None,
    get_session_year=None,
    students=None,
    
    if action is not None:
        if request.method == "POST":
            subject_id=request.POST.get('subject_id')
            session_year_id=request.POST.get('session_year_id')
            
            get_subject=Subject.objects.get(id=subject_id)
            get_session_year=Session_Year.objects.get(id=session_year_id)
            
            subject=Subject.objects.filter(id=subject_id)
            for i in subject:
                student_id=i.course.id
                students=Student.objects.filter(course_id=student_id)
            
    context={
        'subject':subject,
        'session_year':sessiom_year,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'action':action,
        'students':students,
    }
    return render(request,'Faculty/takeattendance.html',context)

@login_required(login_url='/')
def saveattendance(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        attendance_date=request.POST.get('attendance_date')
        student_id=request.POST.getlist('student_id')
        
        get_subject=Subject.objects.get(id=subject_id)
        get_session_year=Session_Year.objects.get(id=session_year_id)
        
        attendance=Attendance(
            subject_id=get_subject,
            attendance_date=attendance_date,
            session_year_id=get_session_year,
            
        )
        attendance.save()
        for i in student_id:
            stud_id=i
            int_stud=int(stud_id)
            p_students=Student.objects.get(id=int_stud)
        # attendance_id=Attendance_Report.objects.all()
            attendance_report = Attendance_Report(
            student_id=p_students,
            attendance_id=attendance,
            )
            attendance_report.save()
            
    return redirect('takeattendance')

@login_required(login_url='/')
def facultyviewattendance(request):
    faculty_id=Faculty.objects.get(admin=request.user.id)

    subject=Subject.objects.filter(faculty_id=faculty_id)
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
    return render(request,'Faculty/facultyviewattendance.html',context)

@login_required(login_url='/')
def addresult(request):
    faculty=Faculty.objects.get(admin = request.user.id)
    subjects=Subject.objects.filter(faculty_id=faculty)
    session_year=Session_Year.objects.all()
    action=request.GET.get('action')
    get_subject=None
    get_session_year=None
    students=None
    
    if action is not None:
        if request.method == "POST":
            subject_id=request.POST.get('subject_id')
            session_year_id=request.POST.get('session_year_id')
            
            get_subject=Subject.objects.get(id=subject_id)
            get_session_year=Session_Year.objects.get(id=session_year_id)

            subjects=Subject.objects.filter(id=subject_id)
            for i in subjects:
                student_id=i.course.id
                students=Student.objects.filter(course_id=student_id)
                

    context={
        'subjects':subjects,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'students':students,
        
        
    }
    return render(request,'Faculty/addresult.html',context)

@login_required(login_url='/')
def saveresult(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        internal_one=request.POST.get('internal_one')
        internal_two=request.POST.get('internal_two')
        assignment_mark=request.POST.get('assignment_mark')
        externals=request.POST.get('externals')

        get_student = Student.objects.get(admin = student_id)
        get_subject = Subject.objects.get(id=subject_id)

        check_exist = StudentResult.objects.filter(subject_id=get_subject, student_id=get_student).exists()
        if check_exist:
            result = StudentResult.objects.get(subject_id=get_subject, student_id=get_student)
            result.internal_one=internal_one
            result.internal_two=internal_two
            result.assignment_mark=assignment_mark
            result.externals=externals
            result.save()
            messages.success(request, "Successfully Updated Result")
            return redirect('addresult')
        else:
            result = StudentResult(student_id=get_student, subject_id=get_subject,  externals=externals,
                assignment_mark=assignment_mark,
                internal_one=internal_one,
                internal_two=internal_two,)
            result.save()
            messages.success(request, "Successfully Added Result")
            return redirect('addresult')
    return None
            
        
    