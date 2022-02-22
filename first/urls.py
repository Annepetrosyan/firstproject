from django.urls import path
from first import views


urlpatterns = [
    path('', views.home),
    path('1/', views.welcoming)
]
