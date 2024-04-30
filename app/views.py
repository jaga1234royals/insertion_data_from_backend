from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from app.models import *

def insert_topic(request):
    tn=input('enter topic name: ')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    

    return HttpResponse(f'One {tn} table name  is inserted succesfully')

def insert_webpage(request):
    tn=input('enter topic name : ')

    '''TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()'''

    TO=Topic.objects.get(topic_name=tn)

    n=input('enter a name : ')
    u=input('enter a url : ')

    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()

    return HttpResponse(f'One {n} webpage is inserted successfully')

def insert_access(request):
    tn=input('enter a topic_name : ')

    '''TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()'''

    TO=Topic.objects.get(topic_name=tn)

    n=input('enter a name : ')
    u=input('enter a url : ')

    '''WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()'''

    '''WO=Webpage.objects.get(topic_name=TO,name=n,url=u)'''
    '''we can get error when get method has no matched element or more than one element'''
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()

    d=input('enter a date : ')
    a=input('enter a author : ')

    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()

    return HttpResponse(f'One {a} Access record is inserted Successfully')



def display_topics(request):
    QLTO=Topic.objects.all()
    d={ 'QLTO':QLTO }
    return render(request,'display_topics.html',context=d)

def display_webpage(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def display_access(request):
    QLAO=Webpage.objects.all()
    d={'QLAO':QLAO}
    return render(request,'display_access.html',d)