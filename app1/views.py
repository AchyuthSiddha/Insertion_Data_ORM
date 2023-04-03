from django.shortcuts import render


from django.http import HttpResponse
# Create your views here.

from app1.models import *
def Insert_Topic(request):
    to=input("enter a Topic:")
    TO=Topic.objects.get_or_create(topic_name=to)[0]
    TO.save()
    return HttpResponse("Insert data sucessfully:")


def Insert_Webpage(request):
    to=input("enter a topic:")
    na=input("enter name:")
    ur=input("enter a url:")
    TO=Topic.objects.get_or_create(topic_name=to)[0]
    TO.save()
    wo=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
    wo.save()
    return HttpResponse("inserted data into webpage sucessufully:")


def Insert_Access_Record(request):
    to=input("enter a topic_name")
    na=input('enter a name:')
    ur=input('enter a url:')
    ema=input("enter a email:")
    aut=input("enter a author name:")
    date=input("enter a date:")
    TO=Topic.objects.get_or_create(topic_name=to)[0]
    TO.save()
    wo=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
    wo.save()
    ao=AccessRecord.objects.get_or_create(name=wo,author=aut,date=date)[0]
    ao.save()
    return HttpResponse("data sucessfully inserted in access records")

    




