from django.shortcuts import render

# Create your views here.
def shopping(req):
    return render(req,'shopping.html')