from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm


def index(request):
    context = {"home": "is-active"}
    return render(request, 'pages/index.html', context)


def about(request):
    context = {"about": "is-active"}
    return render(request, 'pages/about.html', context)


def contact(request):
    context = {"contact": "is-active"}
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['burofriesen@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.add_message(request, messages.SUCCESS, 'Message sent!')
    return render(request, "pages/contact.html", {'form': form})


def documentation(request):
    context = {"documentation": "is-active"}
    return render(request, 'pages/documentation.html', context)