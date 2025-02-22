from django.urls import path
from electronic import views

urlpatterns = [
    path('',views.home,name="home")
    
]