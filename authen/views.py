from django.shortcuts import render

# Create your views here.
def loginn(request):
    return render(request,'login.html')
def signupp(request):
    return render(request,'signup.html')

