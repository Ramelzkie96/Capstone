# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 'index' view associated with 'home' name
    path('logout/', views.logoutUser, name='logout'),  # 'logout' view associated with 'logout' name
    path('logbits/', views.login_bits, name='login_bits'),
    path('logfaculty/', views.login_faculty, name='login_faculty'),
    path('bits/', views.bits_required(views.bits), name='bits'),
    path('faculty/', views.faculty_required(views.faculty), name='faculty'),
]
