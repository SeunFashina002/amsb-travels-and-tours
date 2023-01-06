from django.shortcuts import redirect, render
from .utils import send_apply_form, send_now
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User


# Create your views here.

def home(request):

    return render(request, 'home.html')


def education(request):

    return render(request, 'other_pages/education.html')

def business(request):

    return render(request, 'other_pages/business.html')

def medical(request):

    return render(request, 'other_pages/medical.html')

def tourism(request):

    return render(request, 'other_pages/tourism.html')

def success_modal(request):
    # code goes here
    return render(request, 'other_pages/modal.html')


class Login(LoginView):
    template_name = 'authentication/login.html'

class Login(LoginView):
    template_name = 'authentication/login.html'

@login_required(login_url = '/login')    
def agreement(request):
    username = request.user.username
    user = User.objects.get(username=username)
    user_email = user.email

    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        image_url = request.POST.get('image_url')

        if client_name != "":
            send_now(client_name=client_name, image_url=image_url, user_email=user_email)
            return redirect('apply')

        else:
            return redirect('agreement')
        
    return render(request, 'forms/agreement_form.html')



@login_required(login_url = '/login')
def form(request):
    username = request.user.username
    user = User.objects.get(username=username)
    user_email = user.email
    print(user_email)
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        print(gender)
        relationship = request.POST.get('relationship')
        employment = request.POST.get('employment')
        adress = request.POST.get('address')
        citizenship = request.POST.get('citizenship')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        high_school = request.POST.get('high_school')
        post_secondary_sch = request.POST.get('post_secondary_sch')
        work = request.POST.get('work')
        travel = request.POST.get('travel')
        travel_place = request.POST.get('travel_place')
        illness = request.POST.get('illness')
        accomodation = request.POST.get('accomodation')
        native_lang = request.POST.get('native_lang')
        other_lang = request.POST.get('other_lang')
        passport_num = request.POST.get('passport_num')
        issue_date_passport = request.POST.get('issue_date_passport')
        expire_date_passport = request.POST.get('expire_date_passport')
        visa_refusal = request.POST.get('visa_refusal')
        visa_refusal_reason = request.POST.get('visa_refusal_reason')



    
        context = {
            'first_name' : first_name,
            'middle_name' : middle_name,
            'last_name' : last_name, 
            'dob': dob,
            'gender': gender,
            'relationship':relationship,
            'employment' : employment,
            'adress': adress,
            'citizenship': citizenship,
            'email' : email,
            'tel': tel,
            'high_school': high_school,
            'post_secondary_sch': post_secondary_sch,
            'work': work,
            'travel': travel,
            'travel_place':travel_place,
            'illness':illness,
            'accomodation':accomodation,
            'native_lang':native_lang,
            'other_lang':other_lang,
            'passport_num':passport_num,
            'issue_date_passport':issue_date_passport,
            'expire_date_passport':expire_date_passport,
            'visa_refusal':visa_refusal,
            'visa_refusal_reason':visa_refusal_reason

        }

        print(context)
        send_apply_form(payload=context, user_email=user_email)
        return redirect('success')

    return render(request, 'forms/form.html')

def signup(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
            
    else:
        form = RegisterForm()

    context = {
        'form' : form
    }
    return render(request, 'authentication/signup.html', context)