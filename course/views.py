from django.shortcuts import render,redirect 
from rest_framework import generics
from .models import ShortCourse
# from .serializers import ShortCourseSerializer
from django.views.generic import ListView
from django.http import HttpResponse
import os

# class ShortCourseListCreateView(generics.ListCreateAPIView):
#     queryset = ShortCourse.objects.all()
#     print('insideviewwwwwwwwwwwwwwww')
#     serializer_class = ShortCourseSerializer
    

    

#     def create(self, request, *args, **kwargs):
#         print('afterviewwwwwwwwwwwwwwww')
#         amount_values = request.data.getlist('amount_values[]')
#         amount_texts = request.data.getlist('amount_texts[]')
        

#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)

#         # for value, text in zip(amount_values, amount_texts):
#         #     Amount.objects.create(value=value, text=text, short_course=serializer.instance)

#         headers = self.get_success_headers(serializer.data)
#         return render(request, 'users/short-course-view.html')

    
from django.views.generic.edit import CreateView
from .models import ShortCourse, Amount



def ShortCourseCreateView(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('desc')
        status = request.POST.get('status','Enable')
        image = request.FILES.get('image')

      
        short_course = ShortCourse.objects.create(
            title=title,
            subtitle=subtitle,
            description=description,
            status=status,
            image=image
        )

        
        amount_values = request.POST.getlist('amount_values[]')
        amount_texts = request.POST.getlist('amount_texts[]')

        for value, text in zip(amount_values, amount_texts):
            amount = Amount.objects.create(value=value, text=text)
            short_course.amounts.add(amount)  

       
        short_course.save()

        
        return redirect('ShortCourseList')

    return render(request, 'short-course-create.html')


def ShortCourseList(request):
    context={}
    try:
        
        courses=ShortCourse.objects.all().order_by('id')
        context={
            'courses':courses
        }
    except Exception as e:
        print(e)
    
    return render(request, 'users/short-course-view.html',context)     


def ActiveorInactive(request,id):
    try:
        obj=ShortCourse.objects.get(id=id)
        if obj.status=='Enable':
            obj.status='Disable'
        else:
            obj.status='Enable'    
        obj.save()
        
    except Exception as e:
        print(e)    
        return HttpResponse(False)
        
    return redirect('ShortCourseList')  


def EditCourse(request, id):
    context = {}
    course = ShortCourse.objects.get(id=id)
    
    if request.method == 'POST':
        course.title = request.POST['title']
        course.subtitle = request.POST['subtitle']
        course.description = request.POST['desc']
        course.status = request.POST['title']
        amount_array = request.POST['title']
        if request.FILES['image']:
            image = request.FILES.get('image')                   
            course.image = image
        
        course.save()
        return redirect('ShortCourseList')
    context = {
        'course': course,
    }
    return render(request, "users/short-course-edit.html", context)


def DeleteCourse(request,id):
    try:
        obj=ShortCourse.objects.filter(id=id).first()
        obj.delete()
        
    except Exception as e:
        print(e)   
    return redirect('ShortCourseList')     
        
    

