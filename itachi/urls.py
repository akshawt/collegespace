from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,adminviews,facultyviews,studentviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name='home'),
    path('base',views.base, name='base'),
    path('login',views.logins, name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),
    path('adminhome',adminviews.adminhome,name='adminhome'),
    path('profile',views.profile,name='profile'),
    path('profileupdate',views.profileupdate,name='profileupdate'),
    path('addstudent',adminviews.addstudent,name='addstudent'),
    path('viewstudent',adminviews.viewstudent,name='viewstudent'),
    path('editstudent/<str:id>',adminviews.editstudent,name='editstudent'),
    path('updatestudent',adminviews.updatestudent,name='updatestudent'),
    path('deletestudent/<str:admin>',adminviews.deletestudent,name='deletestudent'),
    path('addcourse',adminviews.addcourse,name='addcourse'),
    path('viewcourse',adminviews.viewcourse,name='viewcourse'),
    path('editcourse/<str:id>',adminviews.editcourse,name='editcourse'),
    path('updatecourse',adminviews.updatecourse,name='updatecourse'),
    path('deletecourse/<str:id>',adminviews.deletecourse,name='deletecourse'),
    path('addfaculty',adminviews.addfaculty,name='addfaculty'),
    path('viewfaculty',adminviews.viewfaculty,name='viewfaculty'),
    path('editfaculty/<str:id>',adminviews.editfaculty,name='editfaculty'),
    path('updatefaculty',adminviews.updatefaculty,name='updatefaculty'),
    path('deletefaculty/<str:admin>',adminviews.deletefaculty,name='deletefaculty'),
    path('addsubject',adminviews.addsubject,name='addsubject'),
    path('viewsubject',adminviews.viewsubject,name='viewsubject'),
    path('editsubject/<str:id>',adminviews.editsubject,name='editsubject'),
    path('updatesubject',adminviews.updatesubject,name='updatesubject'),
    path('deletesubject/<str:id>',adminviews.deletesubject,name='deletesubject'),
    path('addsession',adminviews.addsession,name='addsession'),
    path('viewsession',adminviews.viewsession,name='viewsession'),
    path('editsession/<str:id>',adminviews.editsession,name='editsession'),
    path('updatesession',adminviews.updatesession,name='updatesession'),
    path('deletesession/<str:id>',adminviews.deletesession,name='deletesession'),
    path('facultyhome',facultyviews.facultyhome,name='facultyhome'),
    path('takeattendance',facultyviews.takeattendance,name='takeattendance'),
    path('saveattendance',facultyviews.saveattendance,name='saveattendance'),
    path('facultyviewattendance',facultyviews.facultyviewattendance,name='facultyviewattendance'),
    path('addresult',facultyviews.addresult,name='addresult'),
    path('saveresult',facultyviews.saveresult,name='saveresult'),
    path('studenthome',studentviews.studenthome,name='studenthome'),
    path('studentviewattendance',studentviews.studentviewattendance,name='studentviewattendance'),
    path('adminviewattendance',adminviews.adminviewattendance,name='adminviewattendance'),
    path('viewresult',studentviews.viewresult,name='viewresult'),
    path('sendapplication',studentviews.sendapplication,name='sendapplication'),
    path('saveapplication',studentviews.saveapplication,name='saveapplication'),
    path('viewapplication',adminviews.viewapplication,name='viewapplication'),
    path('approveapplication/<str:id>',adminviews.approveapplication,name='approveapplication'),
    path('declineapplication/<str:id>',adminviews.declineapplication,name='declineapplication'),
    
    
    
    
    
    
    
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
