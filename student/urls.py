from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('student/', views.student_list, name='student'),
    path('student/add/', views.student_create, name='student_add'),
    path('student/<int:id>/edit/', views.student_edit, name='student_edit'),
    path('student/<int:id>/delete/', views.student_delete, name='student_delete'),

    path('Attendance/', views.AttendanceView, name='attendance'),

    path('Course/list/', views.courseListView.as_view(), name='course_list'),
    path('Course/add/', views.courseCreateView.as_view(), name='course_add'),
    path('Course/<int:pk>/edit/', views.courseUpdateView.as_view(), name='course_update'),
    path('Course/<int:pk>/delete/', views.courseDeleteView.as_view(), name='course_delete'),
    path('Course/<int:pk>/detail/', views.courseDetailView.as_view(), name='course_detail'),

    path('dept/list/', views.dept_list, name='dept_list'),

    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),

    path('demo/',views.ajax_demo,name="demo"),
]