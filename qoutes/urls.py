from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home.html',views.index, name="index"),
    path('english.html', views.english, name="english"),
    path('bangla.html', views.bangla, name="index"),
    path('about.html', views.about, name='about')
]
