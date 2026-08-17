from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.CharField(max_length=15)
    city=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20,unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    faculty_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.course_name

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ] 
    student = models.ForeignKey(
        'Student',
        on_delete=models.CASCADE
    )
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )
    remarks = models.CharField(
        max_length=100,
        blank=True, 
        null=True
    )
    def __str__(self):
        return f"{self.student} - {self.date}"

class dept(models.Model):

    department_name=models.CharField(max_length=100)
    HOD_name=models.CharField(max_length=100)
    supervisor_name=models.CharField(max_length=100)
    code=models.IntegerField()

    def __str__(self):
        return self.department_name