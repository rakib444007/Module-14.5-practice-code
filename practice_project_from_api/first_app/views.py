from django.shortcuts import render,redirect
from first_app.forms import ContactForm
from django.http import HttpResponse
# Create your views here.
from first_app.forms import PasswordValidationForm

def DjangoForm(request):
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination: #it is used when we use FileField
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            return redirect('DjangoForm')
    else:
        form = ContactForm()
    return render(request,'django.html',{'form' : form})


def PasswordForm(request):
    if request.method == 'POST':
        form = PasswordValidationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'django.html',{'form': form})
    else:
        form = PasswordValidationForm()
    return render(request,'django.html',{'form': form})
