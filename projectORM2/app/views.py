from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.

def insert_topic(req):
    tn = input("Enter topic:")
    tod = Topic.objects.get_or_create(topic_name=tn)
    print(tod)
    if tod[1]:
        return HttpResponse("New Topic is created.")
    else:
        return HttpResponse("Topic is already present.")
    
def insert_webpage(req):
    id = int(input("enter id:"))
    tn = input("Enter topic")
    name = input("Enter name:")
    url = input("Enter url:")
    email = input("Enter email:")
    LTO = Topic.objects.filter(topic_name=tn)
    if LTO:
        wod = Webpage.objects.get_or_create(id=id,topic_name=LTO[0],name=name,url=url,email=email)
        print(wod)
        if wod[1]:
            return HttpResponse("Webpage is inserted.")
        else:
            return HttpResponse("Webpage is already present.")
    else:
        return HttpResponse("Topic is not present in our databse.")
    
def display_topic(req):
    LTO = Topic.objects.all()
    d={'LTO':LTO}
    return render(req,'display_topic.html',d)

def display_webpage(req):
    LWO = Webpage.objects.all()
    d={'LWO':LWO}
    return render(req,'display_webpage.html',d)
    