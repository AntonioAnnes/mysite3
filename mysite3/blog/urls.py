from django.urls import path

from mysite3.blog import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]
