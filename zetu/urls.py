from django.urls import path, include
from . import views

urlpatterns = [
     path('',views.index, name='home'),
     path('signup/', views.signup, name='signup'),
     path('account/', include('django.contrib.auth.urls')),
     path('profile/<username>/', views.profile, name='profile'),
     path('user_profile/<username>/', views.user_profile, name='user_profile'),
     path('like', views.like_post, name='like_post'),
    path('search/', views.search_profile, name='search'),
]
