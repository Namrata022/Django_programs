from django import forms
from .models import student,Course


class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields ="__all__"

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields ="__all__"