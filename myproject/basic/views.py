from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html')
def aboutus(request):
    return render(request,'aboutus.html')
def services(request):
    return render(request,'services.html')
def contactus(request):
    return render(request,'contactus.html')
def index(request):
    return render(request,'index.html')