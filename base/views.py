from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.db import IntegrityError, transaction

import dateutil.parser
from .forms import ShuttleCheckInForm
from urllib.parse import urlencode
from django.utils import timezone
import datetime

def homeView(request):
    iter_range = [0, 1, 2, 3, 4, 5]

    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ShuttleCheckInForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            shuttle_checkIn = form.save(commit=False)
            print(shuttle_checkIn.staff_id)
            shuttle_checkIn.vehicle_id = "WWT2306"
            shuttle_checkIn.boarding_time = datetime.datetime.now()
            shuttle_checkIn.save()
            print(shuttle_checkIn)
            staff_id_params = urlencode({'vehicle_id': shuttle_checkIn.vehicle_id})
            return HttpResponseRedirect('success?{}'.format(staff_id_params))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ShuttleCheckInForm()

    context = {
        'range' : iter_range,
        'form' : ShuttleCheckInForm
    }

    return render(request, 'base/home.html', context)

def confirmView(request):
    staff_id = request.GET.get('staff_id')
    context = {
        'staff_id' : staff_id,
        'vehicle_id': 'WWT2306'
    }

    return render(request, 'base/confirm.html', context)

def successView(request):
    vehicle_id = request.GET.get('vehicle_id')
    boarding_time = datetime.datetime.now()
    print(boarding_time)
    context = {
        'boarding_time' : boarding_time,
        'vehicle_id': vehicle_id
    }

    return render(request, 'base/success.html', context)