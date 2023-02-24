from django.shortcuts import render,redirect
from . models import *

# Create your views here.

def register(request):
    message = ""
    if request.method == "POST":
        s_name = request.POST['sname']
        s_contact = request.POST['scontact']
        s_email = request.POST['semail']
        s_username = request.POST['susername']
        s_password = request.POST['spassword']
        s_confirmpassword = request.POST['sconfirmpassword']
        s_usertype = 'student'
        s_status = 'active'
        student_data = RegisterStudent(st_name = s_name, st_contact = s_contact, st_email = s_email, st_username = s_username, st_password = s_password, st_confirmpassword = s_confirmpassword, st_usertype = s_usertype, st_status = s_status)
        student_data.save()
        if student_data:
            message = "Student registered successfully"
        else:
            message = "error"    
    return render (request, "database/register.html",{'msg':message})

def login(request):
    if request.method == 'POST':
        user_name = request.POST['logusername']
        pass_word = request.POST['logpassword']
        try:
            reg = RegisterStudent.objects.get(st_username = user_name, st_password = pass_word)
            request.session['testfile_id'] = reg.id
            if reg.st_usertype == 'student' and reg.st_status == 'active':
                return redirect ('student:sthomepage')
            elif(reg.st_usertype == 'admin'):
                return redirect ('student:adhomepage')
            else:
                return render (request, "database/login.html", {'fail':'You are inactive. Unable to Login'})
        except RegisterStudent.DoesNotExist:
            return render (request, "database/login.html", {'fail':'No user found'}) 
               
    return render (request, "database/login.html")

def StHomepage(request):
    if 'testfile_id' in request.session:
        s_id = request.session['testfile_id']
        student = RegisterStudent.objects.get(id = s_id)
        return render (request, "database/studenthome.html", {'student_data':student})
    else:
        return render (request, "database/login.html")     
    
def AdHomepage(request):
    if 'testfile_id' in request.session:
        return render (request, "database/adminhome.html")
    else:
        return render (request, "database/login.html")         
    
def logout(request):
    del request.session['testfile_id']
    return redirect ('student:login')    

def updatestudent(request,s_id):
    if request.method == 'POST':
        name = request.POST['upname']
        contact = request.POST['upcontact']
        email = request.POST['upemail']
        username = request.POST['upusername']
        password = request.POST['uppassword']
        RegisterStudent.objects.filter(id = s_id).update(st_name = name, st_contact = contact, st_email = email, st_username = username, st_password = password)
        return redirect ('student:sthomepage')
    else:
        student_data = RegisterStudent.objects.get(id = s_id)
        return render (request, "database/StudentUpdate.html", {'student': student_data})   

def getstudents(request):  
    student_data1 = RegisterStudent.objects.filter(st_usertype = 'student').values()
    return render (request,"database/StudentStatus.html", {'std_data':student_data1})

def studentstatus(request,s_id):
    status = RegisterStudent.objects.get(id = s_id)
    if status.st_status == 'active':
        RegisterStudent.objects.filter(id = s_id).update(st_status = 'inactive')
        return redirect ('student:studentlist')
    elif (status.st_status == 'inactive'):
        RegisterStudent.objects.filter(id = s_id).update(st_status = 'active')
        return redirect ('student:studentlist')
    # return render (request, "database/StudentStatus.html", {'st_status':status})

