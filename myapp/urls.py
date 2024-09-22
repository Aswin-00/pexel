from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('gallery/', views.Gallery, name='gallery'),

# images url
    path('images/', views.ImageListView.as_view(), name='image_list'),
    path('images/upload/', views.ImageCreateView.as_view(), name='image_upload'),
    path('images/<int:pk>/delete/', views.ImageDeleteView.as_view(), name='image_delete'),
# search
    path('search/', views.search, name='search'),
#images view
    path('image_view/<int:pk>/',views.Imageview, name='image_view'),
    
# non login user
    path('user_profile/<int:pk>/',views.profile_view, name='profile_view'),


]

