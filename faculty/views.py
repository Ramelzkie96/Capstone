# views.py

from django.shortcuts import render, redirect
from .models import Student

def dashboard(request):
    return render(request, 'faculty_dashboard.html')

def student_record_view(request):
    return render(request, 'student_record.html')

def borrow(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        course = request.POST.get('course')
        year = request.POST.get('year')
        description = request.POST.get('description')

        student = Student.objects.create(
            student_id=student_id,
            first_name=first_name,
            last_name=last_name,
            course=course,  # Save the selected course to the database
            year=year,
            status='Borrowed',
            description=description
        )

        return redirect('borrow_success')  
    else:
        return render(request, 'borrow.html')

def borrow_success(request):
    return render(request, 'borrow.html')
