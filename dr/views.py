from django.db.models import QuerySet
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail

# Create your views here.
from .models import pat_ap


def patient(request, usr=None):
    if usr == None:
        return render(request, 'patients/index.html')
    else:

        return render(request, 'patients/index.html', {'usr': usr})

def login(request, i='None'):
    # login for doctor
    if i == 'doc' and request.method == 'POST':
        tab = d_det
        username = request.POST['username']
        pwd = request.POST['pwd']
        if tab.objects.filter(username=username).exists():
            a = tab.objects.get(username=username)
            if pwd == a.password:
                return redirect('doctor', username)
                # return render(request, 'doctor/index.html', {'usr': username, })
            else:
                return render(request, 'login.html', {'pwd_err': 'Incorrect password'})
        else:
            return render(request, 'login.html', {'usr_err': "Username doesn't exist"})
    # login for patients
    elif i == 'pat' and request.method == 'POST':
        tab = p_det
        username = request.POST['username']
        pwd = request.POST['pwd']
        if tab.objects.filter(username=username).exists():
            a = tab.objects.get(username=username)
            if pwd == a.password:
                ap = pat_ap.objects.filter(name=username)
                # return redirect(patient, username)
                return render(request, 'patients/index.html', {'usr': username, 'ap': ap})
            else:
                return render(request, 'login.html', {'pwd_err': 'Incorrect password'})
        else:
            return render(request, 'login.html', {'usr_err': "Username doesn't exist"})
    else:
        return render(request, 'login.html')


# def patient(request, msg='null'):
#     #print('jhvsdjf', request.session.get("doc_id"))
#     # id=request.session["doc_id"]
#     #a=d_profile.objects.get(pk=55)
#     a=d_profile.objects.all()
#     print(a)
#     if msg == 'null':
#         return render(request, 'patients/index.html',{'a': a})
#     else:
#         return render(request, 'patients/index.html', {'msg': msg,'a': a})
def signin(request, i='None'):
    if i == 'doc':
        tab = d_det
    elif i == 'none':
        return render(request, 'login.html')
    else:
        tab = p_det
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['your_email']
        pwd = request.POST['password']
        cnfrm = request.POST['confirm']
        mobile = request.POST['mobile']
        if tab.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'usr_err': 'Username already exists!!', 'username': username})
        elif tab.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'email_err': 'Email is already exits!!!', 'username': username})
        elif pwd != cnfrm:
            return render(request, 'signup.html',
                          {'pwd_err': 'Password mismatch', 'username': username, 'email': email})
        else:
            tab.objects.create(username=username, email=email, password=pwd, mobile=mobile)
            if tab == p_det:
                print(tab)
                return render(request, 'login.html', {'username': username, 'msg': 'username is submitted'})
            else:
                print(tab)
                return render(request, 'doctor/form.html', {'username': username, 'email': email, 'mobile': mobile})
    else:
        return render(request, 'signup.html')




# def doctor(request, usr=None):
#     if d_profile.objects.filter(username=usr).exists():
#         det = d_profile.objects.get(username=usr).department
#         ap = pat_ap.objects.filter(dept=det)
#         p = pat_ap.objects.all()
#         # d=d_det.objects.get(username = usr)
#         return render(request, 'doctor/index.html', {'usr': usr, 'p': p, 'ap': ap})
#     else:
#         return render(request, 'doctor/form.html' ,{'username': usr})

def doctor(request, usr=None):
    if d_profile.objects.filter(username=usr).exists():
        det = d_profile.objects.get(username=usr).department
        ap = pat_ap.objects.filter(dept=det, doc_name='NULL')
        return render(request, 'doctor/index.html', {'usr': usr, 'ap': ap})
    else:
       return render(request, 'doctor/form.html' ,{'username': usr})


def patients_doc(request, usr=None):
    p = pat_ap.objects.all().values_list('name', 'age', 'address', 'mob_no').distinct()
    return render(request, 'doctor/patients.html', {'usr': usr, 'p': p})


def schedule_doc(request, usr=None):
    a = pat_ap.objects.filter(doc_name=usr)
    return render(request, 'doctor/schedule.html', {'usr': usr, 'a': a})


# def all_doctors(request):
#     dp = d_profile.objects.all()
#     print(dp)
#     # request.session["doc_id"]=id_no
#     # return render(request, 'patients/index.html', {'a': a})
#     return render(request, 'patients/doctor.html', {'dp': dp})

def all_doctors(request, usr=None):
    dp = d_profile.objects.filter(verified='YES')
    return render(request, 'patients/doctor.html', {'usr': usr, 'dp': dp})

def doc_profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        prof_pic = request.FILES['prof_pic']
        gender = request.POST['gender']
        dob = request.POST['dob']
        door_no = request.POST['door_no']
        st_name = request.POST['st_name']
        area = request.POST['area']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']
        degree = request.POST['degree']
        department = request.POST['department']
        exp = request.POST['exp']
        id_no = request.POST['id_no']
        id_proof = request.FILES['id_proof']
        hos_name = request.POST['hos_name']
        hos_door_no = request.POST['hos_door_no']
        hos_st_name = request.POST['hos_st_name']
        hos_area = request.POST['hos_area']
        hos_city = request.POST['hos_city']
        hos_state = request.POST['hos_state']
        hos_zip_code = request.POST['hos_zip_code']
        if d_profile.objects.filter(id_no=id_no).exists():
            return render(request, 'doctor/form.html', {'id_no': 'id no already exists!!'})
        else:
            d_profile.objects.create(username=username, email=email, mobile=mobile, prof_pic=prof_pic, gender=gender,
                                     dob=dob, door_no=door_no, st_name=st_name, area=area, city=city, state=state,
                                     zip_code=zip_code, degree=degree, department=department, exp=exp, id_no=id_no,
                                     id_proof=id_proof, hos_name=hos_name, hos_door_no=hos_door_no,
                                     hos_st_name=hos_st_name, hos_area=hos_area, hos_city=hos_city, hos_state=hos_state,
                                     hos_zip_code=hos_zip_code)
            # a = d_profile.objects.get(pk=id_no)
            a = d_profile.objects.all()
            print(a)
            request.session["doc_id"] = id_no
            return render(request, 'patients/index.html', {'a': a})
            # return redirect("patient")


# def ap_det(request):
#     if request.method == 'POST':
#         name = request.POST['p_name']
#         age = request.POST['age']
#         dept = request.POST['dept']
#         mob_no = request.POST['mob_no']
#         date = request.POST['date']
#         time = request.POST['time']
#         address = request.POST['address'] + ", " + request.POST['city'] + ", " + request.POST['state'] + ", " + \
#                   request.POST['zipcode']
#         message = request.POST['message']
#         pat_ap.objects.create(name=name, age=age, dept=dept, mob_no=mob_no, date=date, time=time, address=address,
#                               message=message, doc_name='NULL')
#         ap = pat_ap.objects.filter(name=name)
#         return render(request, 'patients/index.html', {'usr': name, 'ap': ap, 'msg': 'Submitted'})
#     else:
#         return render(request, 'patients/index.html')



def ap_det(request):
    if request.method == 'POST':
        name = request.POST['p_name']
        age = request.POST['age']
        dept = request.POST['dept']
        mob_no = request.POST['mob_no']
        date = request.POST['date']
        time = request.POST['time']
        address = request.POST['address'] + ", " + request.POST['city'] + ", " + request.POST['state'] + ", " + \
                  request.POST['zipcode']
        message = request.POST['message']
        pat_ap.objects.create(name=name, age=age, dept=dept, mob_no=mob_no, date=date, time=time, address=address,
                              message=message, doc_name='NULL')
        ap = pat_ap.objects.filter(name=name)
        return render(request, 'patients/index.html', {'usr': name, 'ap': ap, 'msg': 'Submitted'})
    else:
        return render(request, 'patients/index.html')

# used to send email
def ap_fix(request, usr=None, i=None):
    a = pat_ap.objects.get(ap_no=i)
    a.doc_name = usr
    a.save(update_fields=['doc_name'])
    b = p_det.objects.get(username=a.name).email
    c = d_det.objects.get(username=a.doc_name).email



    send_mail(
            'Appointment Details',
            'Dr '+a.doc_name+', patient name '+a.name+' appointment at '+a.date+' on '+a.time+' login for more details',
            '', #from mail address
            [b,c],
            fail_silently=False,
            )
    
    return redirect('doctor', usr)























# send_mail(
    #         'Appointment Details',
    #         'Your appointment has been fixed with Dr. '+a.doc_name+' at '+a.date+' on '+a.time+' login for more details',
    #         'reahaansheriff@gmail.com',
    #         [b],
    #         fail_silently=False,
    #         )
    # send_mail(
    #         'Appointment Details',
    #         'Your appointment has been fixed with patient '+a.name+' at '+a.date+' on '+a.time+' login for more details',
    #         'reahaansheriff@gmail.com',
    #         [c],
    #         fail_silently=False,
    #         )