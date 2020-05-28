from django.shortcuts import render
from datetime import date
from django.core.mail import EmailMessage
from .forms import *
import time
import smtplib
from . import config
from .models import *


def home(request):
    localtime = time.asctime(time.localtime(time.time()))
    year = int(date.today().year)

    context = {
        'year': year,
        'localtime': localtime,
    }

    return render(request, 'core/home.html', context)


def work(request):
    localtime = time.asctime(time.localtime(time.time()))
    year = int(date.today().year)
    jobs = Job.objects.all()

    context = {
        'year': year,
        'localtime': localtime,
        'jobs': jobs,
    }

    return render(request, 'core/work.html', context)


def about(request):

    edad = int(date.today().year)-1995
    exp = int(date.today().year)-2017
    year = int(date.today().year)
    localtime = time.asctime(time.localtime(time.time()))

    context = {
        'edad': edad,
        'exp': exp,
        'year': year,
        'localtime': localtime,
    }

    return render(request, 'core/about.html', context)


def portfolio(request):
    # year = int(date.today().year)
    # localtime = time.asctime(time.localtime(time.time()))
    # projects = Project.objects.all()
    # jobs = Job.objects.all()

    context = {
        # 'year': year,
        # 'localtime': localtime,
        # 'projects': projects,
        # 'jobs': jobs,
    }

    return render(request, 'core/portfolio.html', context)


def contact(request):

    year = int(date.today().year)
    localtime = time.asctime(time.localtime(time.time()))
    form = Contact(request.POST or None)
    context = {
        'year': year,
        'localtime': localtime,
        'form': form,
    }

    if form.is_valid():
        context = {
            'form': form,
        }
        Full_Name = form.cleaned_data.get("Full_Name")
        Email = form.cleaned_data.get("Email")
        Phone_number = form.cleaned_data.get("Phone_number")
        Message = form.cleaned_data.get("Message")

        title = 'Client: ' + Full_Name
        body = Full_Name + ' ' + Email + ' ' + Phone_number + ' ' + Message + '\n\n  © 2020 · Joyce Gonzalez web page'

        print(title, body)
        email = EmailMessage(title, body, to=['jgonzalezm4d@gmail.com'])
        email.send()

        form = Contact

    return render(request, 'core/contact.html', context)
