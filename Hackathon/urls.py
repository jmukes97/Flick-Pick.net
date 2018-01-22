"""Hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Website import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage),
    path('Actors/', views.PickActors),
    path('LoadActors0/', views.LoadActors0),
    path('LoadActors1/', views.LoadActors1),
    path('LoadActors2/', views.LoadActors2),
    path('Genre/', views.PickGenre),
    path('LoadGenres0/', views.LoadGenres0),
    path('LoadGenres1/', views.LoadGenres1),
    path('LoadGenres2/', views.LoadGenres2),
    path('G-rating/', views.babies),
    path('PG-13/', views.teens),
    path('R-rating/', views.adults),
    path('PG-Rating/', views.kids),
    path('Content-Rating/', views.PickContentRating),
    path("done/", views.done),
    path("Done/", views.Done),
    path("All-done/", views.Alldone),
]
