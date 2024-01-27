from django.shortcuts import render,redirect
from login.models import Register, Products
import random
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.contrib import messages

def generate_otp():
    return str(random.randint(100000, 999999))


def register(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_phone = request.POST.get('user_phone')
        user_dob = request.POST.get('user_dob')
        gender = request.POST.get('gender')
        aadhar = request.POST.get('aadhar')
        pan = request.POST.get('pan')
        marital_status = request.POST.get('marital_status')
        address = request.POST.get('address')
        city = request.POST.get('city')
        district = request.POST.get('district')
        state = request.POST.get('state')
        country = request.POST.get('country')
        pin_code = request.POST.get('pin_code')

        data = Register(
            user_name = user_name,
            user_email = user_email,
            user_phone = user_phone,
            user_dob = user_dob,
            gender = gender,
            aadhar = aadhar,
            pan = pan,
            marital_status = marital_status,
            address = address,
            city = city,
            district = district,
            state = state,
            country = country,
            pin_code = pin_code
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
        email_store = request.session.get('enter_email')
        print(email_store)
        stored_otp = request.session.get('OTP')

        if user_entered_otp == stored_otp :
            data = Register.objects.filter(user_email=email_store)
            print(data)
            context = {'data':data}
            if len(data) is not 0:
                print('yes')
                return render(request,'view_profile.html',context)
        else:
            messages.error(request, 'Please enter valid OTP!')
            return redirect('otp_verify')

    return render(request, 'otp_verfication.html')


def home_page(request):
    email_store = request.session.get('enter_email')
    print(email_store)

    data = Register.objects.filter(user_email=email_store)
    print(data)
    context = {'data':data}
    if len(data) is not 0:
        print('yes')
        return render(request, 'HomePage.html',context)


def user_logout(request):
    logout(request)

    if 'OTP' in request.session:
        del request.session['OTP']

    if 'user_email' in request.session:
        del request.session['user_email']

    return redirect('login')


def update(request,user_id):
    data = Register.objects.get(user_id=user_id)
    if request.method=="POST":
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_phone = request.POST.get('user_phone')
        gender = request.POST.get('gender')
        aadhar = request.POST.get('aadhar')
        pan = request.POST.get('pan')
        marital_status = request.POST.get('marital_status')
        address = request.POST.get('address')
        city = request.POST.get('city')
        district = request.POST.get('district')
        state = request.POST.get('state')
        country = request.POST.get('country')
        pin_code = request.POST.get('pin_code')
        user_dob = request.POST.get('user_dob')

        Data = Register(
            user_id=user_id,
            user_dob=user_dob,
            user_name =user_name,
            user_email =user_email,
            user_phone =user_phone,
            gender =gender,
            aadhar =aadhar,
            pan =pan,
            marital_status =marital_status,
            address =address,
            city =city,
            district =district,
            state =state,
            country =country,
            pin_code =pin_code
                
        )
        Data.save()
        return redirect('view_profile')
    
    return render(request, 'profile.html',{'data':data})



def web_base(request):
    email_store = request.session.get('enter_email')
    print(email_store)

    data = Register.objects.filter(user_email=email_store)
    print(data)
    context = {'data':data}
    if len(data) is not 0:
        print('yes')
        return render(request, 'web_base.html', context)


def view_profile(request):
    email_store = request.session.get('enter_email')
    print(email_store)

    data = Register.objects.filter(user_email=email_store)
    print(data)
    context = {'data':data}
    if len(data) is not 0:
        print('yes')
        return render(request,'view_profile.html',context)


def product_update(request,product_id):

    correct = Products.objects.get(product_id=product_id)
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        hsn_code = request.POST.get('hsn_code')
        manufacture_date = request.POST.get('manufacture_date')
        expiry_date = request.POST.get('expiry_date')
        created_datetime = request.POST.get('created_datetime')
        updated_datetime = request.POST.get('updated_datetime')
        created_by_id = request.POST.get('created_by')
        create = Register.objects.get(user_id=created_by_id)

        new_product = Products(
            product_id=product_id,
            product_name=product_name,
            product_price=product_price,
            hsn_code=hsn_code,
            manufacture_date=manufacture_date,
            expiry_date=expiry_date,
            created_datetime=created_datetime,
            updated_datetime=updated_datetime,
            created_by=create,
        )
        new_product.save()
        return redirect('product')
    
    context = {
        'companies':Register.objects.all(),
        'correct':correct
    }
        
    return render(request, 'products/product_update.html',context)



def product_create(request):
    create_product = Products.objects.all()
    
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        hsn_code = request.POST.get('hsn_code')
        manufacture_date = request.POST.get('manufacture_date')
        expiry_date = request.POST.get('expiry_date')
        created_datetime = request.POST.get('created_datetime')
        updated_datetime = request.POST.get('updated_datetime')
        created_by_id = request.POST.get('created_by')
        create = Register.objects.get(user_id=created_by_id)

        new_product = Products(
            product_name=product_name,
            product_price=product_price,
            hsn_code=hsn_code,
            manufacture_date=manufacture_date,
            expiry_date=expiry_date,
            created_datetime=created_datetime,
            updated_datetime=updated_datetime,
            created_by=create
        )
        new_product.save()
        return redirect('product') 

    return render(request, 'products/product_create.html',{'companies':Register.objects.all()})



# def product(request):
#     product_details = Products.objects.all()

#     print(product_details)
#     return render(request, 'products/products.html',{'products':product_details})

def product(request):
    product_details = Products.objects.all()
    email_store = request.session.get('enter_email')
    print(email_store)

    data = Register.objects.filter(user_email=email_store)
    print(data)
    context = {'data':data,'products':product_details}
    if len(data) is not 0:
        print('yes')
        return render(request, 'products/products.html', context)


def delete(request, product_id):
    data = Products.objects.get(product_id=product_id)
    data.delete()
    return redirect('product')
    