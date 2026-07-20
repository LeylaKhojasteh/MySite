from dataclasses import fields

from django.http import HttpResponseRedirect
from django.shortcuts import render
from website.forms import NameForm,ContactForm, NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request,'website/index.html')


def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = 'unknown'
            contact.save()

            messages.add_message(request, messages.SUCCESS, 'Your message has submitted successfully!')
        else: 
            messages.add_message(request,messages.ERROR,'your ticket didnt submitted.... please try again')
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})



def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print('true')
        else:
            print('false')

    form = ContactForm()
    return render(request,'test.html',{'form':form})