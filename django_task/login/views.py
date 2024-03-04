from django.shortcuts import render,redirect
from login.models import Register, Products
import random
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.contrib import messages


# Generate random otp for login verification
def generate_otp():
    return str(random.randint(100000, 999999))


# Register here users all data
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



# Send otp on user register email

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



# verify here user enter otp and generated otp
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
                return render(request,'HomePage.html',context)
        else:
            messages.error(request, 'Please enter valid OTP!')
            return redirect('otp_verify')

    return render(request, 'otp_verfication.html')


# render user all template data on
def web_base(request, user_id):
    data = Register.objects.filter(user_id=user_id)
    return render(request, 'web_base.html', {'data': data})

# render user data on template
def home_page(request):
    email_store = request.session.get('enter_email')
    print(email_store)

    data = Register.objects.filter(user_email=email_store)
    print(data)
    context = {'data':data}
    if len(data) is not 0:
        print('yes')
        return render(request, 'HomePage.html',context)

# I have provided here logout option to user
def user_logout(request):
    logout(request)

    if 'OTP' in request.session:
        del request.session['OTP']

    if 'user_email' in request.session:
        del request.session['user_email']

    return redirect('login')


# render all updated data on template
def update(request):
    data = Register.objects.all()
    return render(request, 'profile.html',{'data':data})


# here user can update their data using this
def update(request,user_id):
    Data_up = Register.objects.get(user_id=user_id)
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

        Data_up = Register(
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
        Data_up.save()
        return redirect('view_profile')
    
    return render(request, 'profile.html',{'Data_up':Data_up})


# render here common pase base.html
def web_base(request):
    email_store = request.session.get('enter_email')
    print(email_store)

    data = Register.objects.filter(user_email=email_store)
    print(data)
    context = {'data':data}
    if len(data) is not 0:
        print('yes')
        return render(request, 'web_base.html')


# detrieve profile data from database as per user id
def view_profile(request):
    email_store = request.session.get('enter_email')
    print(email_store)

    data = Register.objects.filter(user_email=email_store)
    print(data)
    context = {'data':data}
    if len(data) is not 0:
        print('yes')
        return render(request,'view_profile.html',context)


# retrieve data of product detail from database
def product_details(request):
    email_store = request.session.get('enter_email')
    user_data = Register.objects.filter(user_email=email_store)

    if user_data.exists():
        user_id = user_data.first().user_id

        product_details = Products.objects.filter(created_by_id=user_id)
        
        context = {
            'data': user_data,
            'products': product_details,
        }

        if len(user_data) != 0:
            return render(request, 'products/products.html', context)


# Create product details 
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


# Update product data which in database
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


# Delete product details from here
def delete(request, product_id):
    data = Products.objects.get(product_id=product_id)
    data.delete()
    return redirect('product')    