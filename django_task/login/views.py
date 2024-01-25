from django.shortcuts import render,redirect
from login.models import Register
import random
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.contrib import messages

def generate_otp():
    return str(random.randint(100000, 999999))


def register(request):
    correct = Register.objects.all()
    correct = {
        'correct':correct
    }
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_phone = request.POST.get('user_phone')
        user_dob = request.POST.get('user_dob')
        data = Register(
            user_name = user_name,
            user_email = user_email,
            user_phone = user_phone,
            user_dob = user_dob,
        )

        data.save()


        
        return redirect('login')

    return render(request, 'register.html')


def login(request):
    context ={}

    if request.method == 'POST':
        enter_email = request.POST.get('enter_email')

        try:
            user = Register.objects.get(user_email=enter_email)
        except Register.DoesNotExist:
            messages.error(request, 'Please enter valid email!')
            return redirect('login')

        context = {
            'enter_email': enter_email,
            'user_email': user.user_email,
        }

        OTP = generate_otp()
        email_subject = 'This Message For OTP Authentication'
        email_message =  f'Use the following One Time Password(OTP) for Login.....\n\n{OTP}'
        send_mail(
            email_subject,
            email_message,
            '{{user_email}}',
            [enter_email],
            fail_silently=False,
        )

        request.session['OTP'] = OTP
        request.session['enter_email'] = enter_email

        return redirect('otp_verify')

    return render(request, "login.html",context)


def otp_verify(request):
    if request.method == "POST":
        user_entered_otp = request.POST.get('OTP')

        stored_otp = request.session.get('OTP')

        if user_entered_otp == stored_otp :
            return redirect("HomePage")
        else:
            messages.error(request, 'Please enter valid OTP!')
            return redirect('otp_verify')

    return render(request, 'otp_verfication.html')


def HomePage(request):
    return render(request, 'HomePage.html')


def user_logout(request):
    logout(request)

    if 'OTP' in request.session:
        del request.session['OTP']

    if 'user_email' in request.session:
        del request.session['user_email']

    return redirect('login')


def profile(request):
    all_data = Register.objects.all()
    context = {
        'all_data': all_data
    }
    print(all_data)
    return render(request, 'profile.html', context)