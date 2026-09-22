from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Course, dept, student, Attendance
from .forms import StudentForm,CourseForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# def home(request):
#     return HttpResponse("<h1 style='color:blue;'>Welcome to Django</h1>")

# Create your views here.

@login_required(login_url='login')
def home(request):
    data = {
        'name': 'Namrata',
        'course': 'Django',
        'college': 'JG university',
    }
    subject = ['Django', 'agile', 'Angular', 'React']
    return render(request, 'index.html', {'data': data, 'subject_list': subject, 'Marks': 85})

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='login')
def student_list(request):
    students = student.objects.all()
    return render(request, 'student_crud/list.html', {'students': students})

# def student_add(request):
#     if request.method == 'POST':
#         # name = request.POST.get('name')
#         # email = request.POST.get('email')
#         # mobile = request.POST.get('mobile')
#         # city = request.POST.get('city')
        
#         student.objects.create(
#             name=request.POST ['name'],
#             email=request.POST ['email'], 
#             mobile=request.POST ['mobile'], 
#             city=request.POST ['city'],)
#         return redirect('student_list')
        
#     return render(request, 'student_crud/add.html')

# # --- UPDATE: Edit  an existing student ---
# def student_edit(request, pk):
#     stud = get_object_or_404(student, pk=pk)
    
#     if request.method == 'POST':
#         stud.name = request.POST.get('name')
#         stud.email = request.POST.get('email')
#         stud.mobile = request.POST.get('mobile')
#         stud.city = request.POST.get('city')
#         stud.save()
#         return redirect('student_list')
        
#     return render(request, 'student_crud/edit.html', {'student': stud})
@login_required(login_url='login')
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form = StudentForm()
    return render(request, 'student_crud/add.html', {'form': form, 'title': 'Add Student'})

@login_required(login_url='login')
def student_edit(request, id):
    student_obj = get_object_or_404(student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student_obj)
        if form.is_valid():
            form.save()
            return redirect('student')
    else: 
        form = StudentForm(instance=student_obj)
    return render(request, 'student_crud/edit.html', {'form': form, 'title': 'Edit Student'})

@login_required(login_url='login')
def student_delete(request, id):
    student_obj = get_object_or_404(student, id=id)
    student_obj.delete()
    return redirect('student')

@login_required(login_url='login')
def AttendanceView(request):
    attendance_list = Attendance.objects.all()
    return render(request, 'student_crud/attendance.html', {'attendences': attendance_list})

@login_required(login_url='login')
def dept_list(request):
    departments = dept.objects.all()
    return render(request, 'dept/list.html', {'departments': departments})

#course View
class courseCreateView(LoginRequiredMixin,CreateView):
    model=Course
    form_class=CourseForm
    template_name='course_crud/course_form.html'
    success_url=reverse_lazy('Course_list')

class courseListView(LoginRequiredMixin,ListView):
    model=Course
    template_name='course_crud/course_list.html'
    context_object_name='courses'

class courseUpdateView(LoginRequiredMixin,UpdateView):
    model=Course
    fields='__all__'
    template_name='course_crud/course_form.html'
    success_url=reverse_lazy('Course_list')

class courseDeleteView(LoginRequiredMixin,DeleteView):
    model=Course
    template_name='course_crud/course_confirm_delete.html'
    success_url=reverse_lazy('Course_list')

class courseDetailView(LoginRequiredMixin,DetailView):
    model=Course
    template_name='course_crud/course_detail.html'


def login_view(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,
                          username=username,
                          password=password
                          )
        if user is not None:
            login(request,user)
            #store the user in the session
            request.session['username']=user.username
            return redirect('home')

        else:
            return render(request,'login.html',{'error':'Invalid username or password'})

    return render(request,'login.html')

def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('login')