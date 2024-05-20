from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('borrow/', views.borrow, name='borrow'),  # Change to end with a slash for consistency
    path('student-record/', views.student_record_view, name='student-record'),
    path('borrow-success/', views.borrow_success, name='borrow_success'),  # Add URL pattern for success page
]
