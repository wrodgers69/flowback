from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse, reverse_lazy
from flowback.forms import CrispyModelForm, CrispyDataForm
from django.views.generic.edit import FormView
from PIL import Image
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
#from flowback.models import Well_Profile, Card_Info, Dysfunction_Profile
from django.views.decorators.csrf import csrf_exempt
from tensorai.settings import *
import jwt

#create views here

class home(View):

    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'flowback/home.html')

class success(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'flowback/success.html')

class logout(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'flowback/logout.html')

class well_information(View):
    @method_decorator(login_required)
    def get(self, request):
        form = CrispyModelForm()
        return render(request, 'flowback/well_information.html', {
        'form': form
        })

    @method_decorator(login_required)
    def post(self, request):
        form = CrispyModelForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('success'))

class well_data(View):
    @method_decorator(login_required)
    def get(self, request):
        form = CrispyDataForm()
        return render(request, 'flowback/inputdata.html', {
        'form': form
        })

    @method_decorator(login_required)
    def post(self, request):
        form = CrispyModelForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('success'))
