from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from . utils import send_now

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


def agreement(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        image_url = request.POST.get('image_url')

        if client_name != "":
            send_now(client_name=client_name, image_url=image_url)

        else:
            return redirect('agreement')
        
    return render(request, 'forms/agreement_form.html')




def form(request):

    return render(request, 'forms/form.html')
