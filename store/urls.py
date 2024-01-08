from django.urls import path

from store import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blog_detaile, name='blog_detaile'),
    path('contact/', views.contact, name='contact'),
    path('project/', views.project, name='project'),
    path('services/', views.services, name='services'),
    path('single/', views.single),
]
