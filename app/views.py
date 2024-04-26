from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from app.models import *

def insert_topic(request):
    tn=input('enter topic name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    return HttpResponse(f'One {tn} is inserted succesfully')

def insert_webpage(request):
    tn=input('enter topic name : ')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    n=input('enter a name : ')
    u=input('enter a url : ')

    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()

    return HttpResponse(f'One {n} is inserted successfully')

def insert_access(request):
    tn=input('enter a topic_name : ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    n=input('enter a name : ')
    u=input('enter a url : ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()

    d=input('enter a date : ')
    a=input('enter a author : ')
    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()

    return HttpResponse(f'One {a} is inserted Successfully')
