from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [ 
   
    path('', LoginView.as_view(), name='user-login'), 
    path('changepwd/',change_passsword.as_view(), name='change_password'), 
    path('dashboard/',dashboard, name='dashboard'),
    path('profile/',profile, name='profile'),
    path('shortCreate/',shortTermCourse, name='short-course-create'),
    path('courseView/',courseView, name='courseView'),
    path('logout/', LogoutView.as_view(next_page='user-login'), name='custom-logout'), 
    

    
]