from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import student, Attendance


class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'email', 'mobile', 'city']


# def home(request):
#     return HttpResponse("<h1 style='color:blue;'>Welcome to Django</h1>")

# Create your views here.


def home(request):
    data = {
        'name': 'Namrata',
        'course': 'Django',
        'college': 'JG university',
    }
    subject = ['Django', 'agile', 'Angular', 'React']
    return render(request, 'index.html', {'data': data, 'subject_list': subject, 'Marks': 85})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    students = student.objects.all()
    return render(request, 'student_crud/list.html', {'students': students})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form = StudentForm()
    return render(request, 'student_crud/add.html', {'form': form, 'title': 'Add Student'})


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



def student_delete(request, id):
    student_obj = get_object_or_404(student, id=id)
    student_obj.delete()
    return redirect('student')


def AttendanceView(request):
    attendance_list = Attendance.objects.all()
    return render(request, 'student_crud/attendance.html', {'attendences': attendance_list})