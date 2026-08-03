from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('student/', views.student_list, name='student'),
    path('add/', views.student_create, name='student_add_short'),
    path('student/add/', views.student_create, name='student_add'),
    path('student/<int:id>/edit/', views.student_edit, name='student_edit'),
    path('student/<int:id>/delete/', views.student_delete, name='student_delete'),
    path('Attendance/', views.AttendanceView, name='Attendance'),
]