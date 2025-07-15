from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('education/', views.education, name='education'),
    path('projects/', views.projects, name='projects'),
    path('achievements/', views.achievements, name='achievements'),
    path('certifications/', views.certifications, name='certifications'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('contact/', views.contact, name='contact'),
] 