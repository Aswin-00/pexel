from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from myapp import views


urlpatterns = [
    path('',include("myapp.urls")),
    # path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('superman', admin.site.urls, name='superman'),
    path('login', views.CustomLoginView.as_view(), name='login_page'),

    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
