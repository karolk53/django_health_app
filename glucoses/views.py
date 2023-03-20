from django.shortcuts import render, redirect
from .forms import GlucosesParametersForm
from .models import GlucosesParameters
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.


@login_required
def measurement_list(request):
    measurements = GlucosesParameters.objects.filter(user__id=request.user.id).order_by('-id')
    p = Paginator(measurements, 5)
    page_number = request.GET.get('page')
    measurements = p.get_page(page_number)
    return render(request,'glucoses/measurement_list.html',{'measurements': measurements})

@login_required
def add_measurement(request):
    if request.method == 'POST':
        form = GlucosesParametersForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request,messages.SUCCESS,"Added successfully!")
            return redirect("glucoses:add")
        else:
            messages.add_message(request, messages.WARNING, "Wrong data!")
    else:
        form = GlucosesParametersForm()
    return render(request,'glucoses/add_measurement.html',{'form': form})