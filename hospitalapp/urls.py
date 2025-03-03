
from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('service/', views.services,name='service-details'),
    path('starter/', views.starter,name='starter'),
    path('about/', views.about,name='about'),
    path('services/', views.service,name='services'),
    path('doctor/', views.doctor,name='doctor'),
    path('department/', views.department,name='department'),
    path('appointment/', views.appoint,name='appointment'),
    path('contact/', views.contacts,name='contact'),
    path('show/', views.show,name='show'),
    path('delete/<int:id>', views.delete),
]
