# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RequestForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.shortcuts import redirect
from django.template import Context

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', context = {})

def contact(request):
    return render(request, 'pages/contact.html', context = {})

def finance(request):
    return render(request, 'pages/finance.html', context = {})

def about(request):
    return render(request, 'pages/about.html', context = {})

def thanks(request):
    return render(request, 'pages/thanks.html', context = { })

def request(request):
    if request.method == 'GET':
        form = RequestForm()
    else:
        form = RequestForm(request.POST)
        if form.is_valid():
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            budget = request.POST.get('budget', '')
            content = request.POST.get('content', '')

            template = get_template('pages/request_template.txt')
            context = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone': phone,
                'budget': budget,
                'content': content
            }
            content = template.render(context)
            email = EmailMessage("Motorcycle Request Form Submission",
                                content,
                                "Your website" +'',
                                ['crao.anshu@gmail.com'],
                                headers = {'Reply-To': email }
            )
            email.send()
            return redirect('pages:thanks')
    return render(request, 'pages/request.html', context = {'form': form})