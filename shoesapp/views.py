from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from random import randrange

# Create your views here.
def registration(request):
    if request.method == 'POST':
        try:
            Register.objects.get(email=request.POST['email'])
            return render(request,'registration.html',{'msg':'Your Email is already registered'})
        except:
            if request.POST['password']==request.POST['cpassword']:
                global temp
                temp={
                    'name' : request.POST['name'],
                    'mobile' : request.POST['mobile'],
                    'email' : request.POST['email'],
                    'address' : request.POST['address'],
                    'password' : request.POST['password']
                }
                otp = randrange(1000,9999)
                subject = 'welcome to Shoes App'
                message = f'Your OTP is {otp}. please enter correctly'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'cotp.html',{'otp':otp})
            return render(request,'login.html',{'msg':'Account is Created'})
    return render(request,'registration.html')

def cotp(request):
    if request.method == 'POST':
        if request.POST['uotp'] == request.POST['otp']:
            global temp
            
            Register.objects.create(
                name = temp['name'],
                email = temp['email'],
                mobile = temp['mobile'],
                address = temp['address'],
                password = temp['password']
            )
            msg = "Account is Created"
            return render(request,'login.html',{'msg':msg})
        return render(request,'cotp.html',{'otp':request.POST['otp'],'msg':'incorrect OTP'})
    return redirect('registration')
    # return render(request,'cotp.html')


def login(request):
    try:
        Register.objects.get(email=request.session['clientemail'])
        return redirect('index')
    except:
        if request.method == 'POST':
            try:
                uid = Register.objects.get(email=request.POST['email'])
                if uid.password == request.POST['password']:
                    request.session['clientemail'] = uid.email
                    return redirect('index')
                return render(request,'login.html',{'msg':'Password is incorrect'})
            except:
                return render(request,'registration.html',{'msg':'Email is not registered'})
        return render(request,'login.html')
def clogout(request):
    del request.session['clientemail']
    return redirect('index')

def index(request):
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        return render(request,'index.html',{'uid':uid})
    except:
        return render(request,'index.html')
def cpassword(request):
    uid = Register.objects.get(email=request.session['clientemail'])
    if request.method == 'POST':
        if uid.password == request.POST['opassword']:
            if request.POST['npassword'] == request.POST['cpassword']:
                uid.password = request.POST['npassword']
                uid.save()
                return redirect('index')
            return render(request,'cpassword.html',{'msg':'Both password are not same'})
        return render(request,'cpassword.html',{'msg':'old password is not correct'})
    return render(request,'cpassword.html')

def contact(request):

    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        if request.method == 'POST':
            Contact.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                subject=request.POST['subject'],
                message=request.POST['message']
            )
            msg='Complant is Added'
            return render(request,'contact.html',{'msg':msg,'uid':uid})
        return render(request,'contact.html',{'uid':uid})
    except:
        if request.method == 'POST':
            Contact.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                subject=request.POST['subject'],
                message=request.POST['message']
            )
            msg='Complant is Added'
            return render(request,'contact.html',{'msg':msg})
        return render(request,'contact.html')
def kid(request):
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        return render(request,'kid.html',{'uid':uid})
    except:
        return render(request,'kid.html')
def about(request):
    return render(request,'about.html')
def men(request):
    return render(request,'men.html')
def checkout(request):
    return render(request,'checkout.html')

def order(request):
    return render(request,'order-complete.html')
def product(request):
    return render(request,'product-detail.html')
def women(request):
    return render(request,'women.html')
def cart(request):
    return render(request,'cart.html')
def add(request):
    return render(request,'add-to-wishlist.html')
