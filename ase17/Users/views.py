from django.shortcuts import  render, redirect
from django.contrib.auth import  authenticate, login
from Users.forms import  RegistrationForm, ProfileRegistrationForm,ProfileUpdateForm
from ase17.urls import *
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, 'Users/index.html')

def register(request):


    if request.method == 'POST':

        uf = RegistrationForm(request.POST, prefix='user')
        upf = ProfileRegistrationForm(request.POST, prefix='userprofile')

        if uf.is_valid() and upf.is_valid():

            password = uf.cleaned_data['confirm_password']
            user = uf.save(commit=False)
            user.set_password(password)
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            login(request, user)
            return redirect('index')
    else:

        uf = RegistrationForm(prefix='user')
        upf = ProfileRegistrationForm(prefix='userprofile')
    context = {'userform': uf, 'userprofileform': upf}
    return render(request, 'registration/register.html', context)

def UpdateProfile(request):


    if request.method == 'POST':

        puf = ProfileUpdateForm(request.POST,instance=request.user.profile)
        if puf.is_valid():
            puf.save()
            return redirect('index')
    else:

        puf = ProfileUpdateForm(instance=request.user.profile)
        context = {'ProfileUpdateForm': puf}
        return render(request, 'Users/ProfileUpdate.html', context)



