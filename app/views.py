from django.shortcuts import render
from django.db.models.functions import Length
from django.http import HttpResponse
# Create your views here.

from app.models import *

def insert_topic(request):
    tn=input('enter topic name: ')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    d={'QLTO':Topic.objects.all()}
    

    return render(request,'display_topics.html',d)

def insert_webpage(request):
    tn=input('enter topic name : ')

    '''TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()'''

    TO=Topic.objects.get(topic_name=tn)

    n=input('enter a name : ')
    u=input('enter a url : ')

    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    d={'QLWO':Webpage.objects.all()}
    return render(request,'display_webpage.html',d)

def insert_access(request):

    '''TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()'''

    n=input('enter a name : ')

    '''WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()'''

    '''WO=Webpage.objects.get(topic_name=TO,name=n,url=u)'''
    '''we can get error when get method has no matched element or more than one element'''
    WO=Webpage.objects.get(name=n)


    d=input('enter a date : ')
    a=input('enter a author : ')

    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()

    d={'QLAO':AccessRecord.objects.all()}
    return render(request,'display_access.html',d)



def display_topics(request):
    QLTO=Topic.objects.all()
    d={ 'QLTO':QLTO }
    return render(request,'display_topics.html',context=d)

def display_webpage(request):
    QLWO=Webpage.objects.all()  # we will get entire table 
    QLWO=Webpage.objects.order_by('name') # we will get entire table in the form of ascending order by using alphabets
    QLWO=Webpage.objects.order_by('-name') # we will get entire table in the form of descending order by using alphabets
    QLWO=Webpage.objects.order_by('name')[:5] # we will 0 to 4 rows(means 5 rows) in the form of ascending order by usnig alphabets
    QLWO=Webpage.objects.order_by('-name')[2:7] # we will 2 to 6 rows(means 5 rows) in the form of descending order by using alphabets
    QLWO=Webpage.objects.order_by(Length('name')) # we will get entire table in the form of ascending order by using length
    QLWO=Webpage.objects.order_by(Length('name').desc()) # we will get entire table in the form of descending order by using length
    QLWO=Webpage.objects.filter(name__startswith='a') # we will get the names of starting character 'a'
    QLWO=Webpage.objects.filter(name__endswith='a') # we will get the names of ending character 'a'
    QLWO=Webpage.objects.filter(name__contains='a') # we will get the names of character 'a' contains anywhere in string

    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def display_access(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.filter(date__year='2024') # we will get the data of year 2024 
    QLAO=AccessRecord.objects.filter(date__month='4') # we will get the data of month april 
    QLAO=AccessRecord.objects.filter(date__day='20') # we will get the data of day 20
    QLAO=AccessRecord.objects.filter(date__year__gt='2020') # we will get the data greater than year 2020
    QLAO=AccessRecord.objects.filter(date__year__lt='2018') # we will get the data less than year 2018
    QLAO=AccessRecord.objects.filter(date__year__gte='2020') # we will get the data greater than or equals to year 2020
    QLAO=AccessRecord.objects.filter(date__year__lte='2018') # we will get the data less than or equals to year 2018
    d={'QLAO':QLAO}
    return render(request,'display_access.html',d)