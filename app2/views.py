from django.shortcuts import render

def app2_home(request):
    return render(request,'app2/app2.html')