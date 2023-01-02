from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from .utils import send_apply_form, send_now
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.views import LoginView

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

class Login(LoginView):
    template_name = 'authentication/login.html'

class Login(LoginView):
    template_name = 'authentication/login.html'
def agreement(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        image_url = request.POST.get('image_url')

        if client_name != "":
            send_now(client_name=client_name, image_url=image_url)

        else:
            return redirect('agreement')
        
    return render(request, 'forms/agreement_form.html')



@login_required(login_url = '/login')
def form(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

    
        context = {
            'first_name' : first_name,
            'last_name' : last_name, 
        }

        send_apply_form(payload=context)

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