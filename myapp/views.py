
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from  .images_views import *
from django.contrib.auth import views as auth_views
from .forms import EmailAuthenticationForm
from .models import Image as ImageModel
from django.db.models import Q
from django.conf import settings
from django.http import JsonResponse
from datetime import datetime




def get_uptime_data(request):
    current_time = datetime.now()
    server_start_time = settings.SERVER_START_TIME
    uptime_duration = current_time - server_start_time

    uptime_seconds = uptime_duration.total_seconds()
    uptime_hours, remainder = divmod(uptime_seconds, 3600)
    uptime_minutes, uptime_seconds = divmod(remainder, 60)

    return JsonResponse({
        'uptime_hours': int(uptime_hours),
        'uptime_minutes': int(uptime_minutes),
        'uptime_seconds': int(uptime_seconds),
    })


#index page
def index(request):
    
        
    
    context={
        'images':ImageModel.objects.all().order_by('-created_at')
    }
    if request.user.is_staff:
        context.update({
            "imagecount":ImageModel.objects.count(),
            "usercount":User.objects.count()
        })
    
    return render(request, 'index.html',context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            
            user = form.save()
            print('asd')

            # login(request, user)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return redirect('profile')  # Redirect to the home page after registration
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required(login_url='login_page')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})



@login_required(login_url='login_page')
def Gallery(request):
    
    context={
        'images':ImageModel.objects.filter(user=request.user).order_by('-created_at')

        
    }
    return render(request, 'gallery.html', context)



class CustomLoginView(auth_views.LoginView):
    form_class = EmailAuthenticationForm
    
    
# search

def search(request):
    query = request.GET.get('word')  # Get 'q' from GET request or use 'word' from URL
    # Filter images based on tags or description matching the word
    print(query)
    if query:
        images = ImageModel.objects.filter(Q(tags__icontains=query) | Q(description__icontains=query))
    else:
        images = ImageModel.objects.none()  # Return empty queryset if no query
    
    
    
    # Prepare the context for rendering
    context = {
        'images': images
    }
    
    return render(request, 'search.html', context)    


# images view
def Imageview(request,pk):
    image=ImageModel.objects.filter(pk=pk)
    print(image)
    context={  
        'image':image[0],
        'all':ImageModel.objects.exclude(pk=pk)
    }
    
    return render(request,'view_image.html',context)


# user profile view for non login user 
def profile_view(request,pk):
    
    context={
        "image":ImageModel.objects.filter(pk=pk)[0],
        "all":ImageModel.objects.filter(pk=pk)


    }
    return render(request,'non_login/profile.html',context)

# tag based search 
def search_tag(request,tag):
    query = tag  
    print(query)
    if query:
        images = ImageModel.objects.filter(Q(tags__icontains=query) | Q(description__icontains=query))
    else:
        images = ImageModel.objects.none()  # Return empty queryset if no query
    
    
    
    # Prepare the context for rendering
    context = {
        'images': images
    }
    
    return render(request, 'search.html', context)    

