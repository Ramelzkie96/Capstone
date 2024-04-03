# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('logout/', views.logoutUser, name='logout'),
    path('bits/', views.bits_required(views.bits), name='bits'),
    path('faculty/', views.faculty_required(views.faculty), name='faculty'),
]
