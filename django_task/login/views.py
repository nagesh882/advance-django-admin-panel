from django.shortcuts import render,redirect,get_object_or_404
from login.models import Register
import random
from django.core.mail import send_mail

def generate_otp():
    return str(random.randint(100000, 999999))

def register(request):
    correct = Register.objects.all()
    correct = {
        'correct':correct
    }
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_phone = request.POST.get('user_phone')
        user_dob = request.POST.get('user_dob')
        data = Register(
            user_id = user_id,
            user_name = user_name,
            user_email = user_email,
            user_phone = user_phone,
            user_dob = user_dob,
        )

        data.save()

        
        OTP = generate_otp()
        email_subject = 'Your Login OTP'
        email_message =  f'User {user_name} has been authenticated, please use the following One Time Password(OTP) for Login\n\n{OTP}'
        send_mail(
            email_subject,
            email_message,
            '{{user_email}}',
            [user_email],
            fail_silently=False,
        )

        request.session['OTP'] = OTP
        request.session['user_email'] = user_email
        
        return redirect('login')

    return render(request, 'register.html')


def login(request):
    context ={}
    if request.method == 'POST':

        user_entered_otp = request.POST.get('OTP')

        stored_otp = request.session.get('OTP')

        print(stored_otp)

        email_store = request.session.get('user_email')

        print(email_store)

        if user_entered_otp == stored_otp :

            data = Register.objects.filter(user_email=email_store)
            print(data)

            return redirect("HomePage")
        
        context = {
            'user_entered_otp':user_entered_otp,
            'email_store':email_store
        }
     
    return render(request, "login.html",context)


def HomePage(request):
    return render(request, 'HomePage.html')

def indexPage(request):
    return render(request, 'index.html')