from django.shortcuts import render

# Create your views here.
def project(req):
    return render(req,'index.html')