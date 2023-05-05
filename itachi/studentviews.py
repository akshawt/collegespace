from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Course,Session_Year,CustomUser,Student,Faculty,Subject,Attendance,Attendance_Report,StudentResult,StudentApplication
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def studenthome(request):
    return render(request,'Student/studenthome.html')


@login_required(login_url='/')
def studentviewattendance(request):
    student=Student.objects.get(admin=request.user.id)
    subjects=Subject.objects.filter(course=student.course_id)
    action=request.GET.get('action')
    get_subject=None
    attendance_report=None
    if action is not None:
        if request.method == "POST":
            subject_id= request.POST.get('subject_id')
            get_subject=Subject.objects.get(id=subject_id)
            
            attendance_report=Attendance_Report.objects.filter(student_id=student,attendance_id__subject_id=subject_id)

    context={
        'subjects':subjects,
        'action':action,
        'get_subject':get_subject,
        'attendance_report':attendance_report,
        
    }
    
    return render(request,'Student/studentviewattendance.html',context)

@login_required(login_url='/')
def viewresult(request):
    mark=None
    student = Student.objects.get(admin=request.user.id)
    result=StudentResult.objects.filter(student_id=student)
    for i in result:
        internal_one =i.internal_one
        internal_two =i.internal_two
        assignment_mark =i.assignment_mark
        externals =i.externals
        
        mark = i.mark =  internal_one +internal_two + assignment_mark + externals -min(internal_one,internal_two,assignment_mark)

    context={
        'result':result,
        'mark':mark,
    }
    return render(request,'Student/viewresult.html',context)

@login_required(login_url='/')
def sendapplication(request):
    student= Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id=i.id
        student_appl_history=StudentApplication.objects.filter(student_id=student_id)
        context={
            'student_appl_history':student_appl_history,
        }
        return render(request,'Student/sendapplication.html',context)

@login_required(login_url='/')
def saveapplication(request):
    if request.method == "POST":
        application_subject=request.POST.get('application_subject')
        message=request.POST.get('message')
        student=Student.objects.get(admin=request.user.id)
        application=StudentApplication(
            student_id=student,
            application_subject=application_subject,
            message=message,
        )
        application.save() 
        messages.success(request,'Application Succesfully Sent !')
        
    return redirect('sendapplication')