
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.views import View
from .serializers import UserLoginSerializer
from django.contrib import messages
from django.http import HttpResponse
from course.models import ShortCourse


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        
        serializer = UserLoginSerializer(data=request.POST)
        if serializer.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            print(email)
            print(password)
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "User login successful")
                request.session['email'] = email
                return render(request,'users/profile.html')

            else:
                messages.error(request, 'Invalid username or password')
        else:
            return render(request, 'users/login.html', {'message': 'Invalid form data.'})

class change_passsword(View):
    def post(self, request):
        # serializer = UserLoginSerializer(data=request.POST)
        # if serializer.is_valid():
        user=request.user
        password=request.POST['password']
        new_password=request.POST['new_password']
        confirmpassword=request.POST['new_conformpassword']
        if new_password == confirmpassword:
            if user.check_password(password):
                user.set_password(new_password)
                user.save()
        return render(request,'users/profile.html')
    
    
def dashboard(request):
        return render(request, 'users/index.html')
def shortTermCourse(request):
        return render(request, 'users/short-course-create.html')    
def profile(request):
        return render(request, 'users/profile.html')    
def courseView(request):
    courses=ShortCourse.objects.all()
    context={
        'courses':courses
    }
    print(context,'context..........')
    return HttpResponse(courses)
    return render(request, 'users/short-course-view.html',context)     
        


