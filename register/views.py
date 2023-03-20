from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('main:home_page'))
        else:
            messages.add_message(request,messages.ERROR,"Incorrect registration data!")
    else:
        form = RegistrationForm()
    return render(request,'register/registration.html',{'form': form})