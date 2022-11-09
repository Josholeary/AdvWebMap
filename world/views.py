import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.gis.geos import Point
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def Vlogin(request):
    if request.method == 'POST':
        lf = LoginForm(data=request.POST)
        if lf.is_valid():
            user = lf.get_user()
            login(request, user)
            return redirect('home')
    else:
        lf = LoginForm()
    return render(request, 'registration/login.html', {'lf': lf})


class Vsignup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def Vhome(request):
    return render(request, 'home.html')


def Vlogout(request):
    logout(request)
    return redirect('home')


@login_required
def add_location_db(request):
    data = json.loads(request.body)
    lon = data['longitude']
    lat = data['latitude']
    my_profile = request.user.profile
    my_profile.last_location = Point(lon, lat)
    my_profile.save()
    print(my_profile.last_location)
    return JsonResponse('Saved', status=200, safe=False)
