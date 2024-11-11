from django.shortcuts import render

# Create your views here.
def First_Page(request):
    return render(request,'Home.html')

def SecondPage(request):
    return render(request,"SecondPage.html")
