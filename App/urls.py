from . import views
from django.urls import path

urlpatterns=[
    path('',views.First_Page,name="First_Page"),
    path('SecondPage',views.SecondPage,name="SecondPage")
]
