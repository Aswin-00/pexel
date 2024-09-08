
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



#index page
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            
            user = form.save()
            print('asd')

            login(request, user)
            return redirect('profile')  # Redirect to the home page after registration
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})



@login_required
def Gallery(request):
    
    context={
        
    }
    return render(request, 'gallery.html', context)