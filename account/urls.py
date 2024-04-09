from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('logout/', views.logoutUser, name='logout'),
    path('bits/', views.bits_required(views.bits), name='bits'),
    path('faculty/', views.faculty_required(views.faculty), name='faculty'),
]
# Add the following line to serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
