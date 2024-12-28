from django.contrib import admin 
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from blog import views


urlpatterns = [
    path('',views.index,name='index'),
    path('blog/<str:slug>/',views.single,name='single'),
    path('blog/',views.blog,name='blog'),
    path('home/',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('category/',views.category,name='category'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('<str:slug>/',views.single,name='single')

   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
