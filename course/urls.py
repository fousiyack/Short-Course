from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.ShortCourseCreateView, name='course-create'),
    # path('courses/<int:pk>/', views.ShortCourseDetailView.as_view(), name='short-course-detail'),
    # path('coursesList', views.ShortCourseList.as_view(), name='coursesList'),
    
    path('ShortCourseList/',views.ShortCourseList, name='ShortCourseList'),
    path('ActiveorInactive/<int:id>/',views.ActiveorInactive, name='ActiveorInactive'),
    path('DeleteCourse/<int:id>/',views.DeleteCourse, name='DeleteCourse'),
    path('EditCourse/<int:id>/',views.EditCourse, name='editCourse'),
    
]
