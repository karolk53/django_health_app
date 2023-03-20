from django.shortcuts import render, redirect
from .forms import BloodPressureParametersForm
from .models import BloodPressureParameters
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

def menu(request):
    return render(request,'bloodpresuers/menu.html',{})


@login_required
def add_survey(request):
    if request.method == "POST":
        form = BloodPressureParametersForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.SUCCESS, "Added successfully!")
            return redirect('bloodpresures:add')
        else:
            messages.add_message(request, messages.WARNING, "Wrong data!")
    else:
        form = BloodPressureParametersForm()
    return render(request, 'bloodpresuers/add_measurement.html', {'form': form})


@login_required
def surveys_list(request):
    measurements = BloodPressureParameters.objects.filter(user__id=request.user.id).order_by("-examination_date")
    p = Paginator(measurements, 5)
    page_number = request.GET.get('page')
    measurements = p.get_page(page_number)
    return render(request, 'bloodpresuers/measurements_list.html', {'measurements': measurements})