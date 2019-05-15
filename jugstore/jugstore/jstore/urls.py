from django.urls import path
from . import views

# Rekisteröinti urli piti laittaa tänne koska käyttäjien luonti on määritelty tässä kansiossa eikä pääkansiossa
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]