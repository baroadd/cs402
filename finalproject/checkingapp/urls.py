from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.index,name ='index'),
    #path('<url>/',views.getparams,name='getparams')
]