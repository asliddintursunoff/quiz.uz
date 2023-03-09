from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from django.http import HttpResponse
from . import models



class FanlarViewSet(ModelViewSet):
    queryset = Fanlar.objects.all()
    serializer_class = FanlarSerializers
    http_method_names = ['get','head']

class LevelViewSet(ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializers
    http_method_names = ['get','head']

class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializers
    http_method_names = ['get','head']
    
# class FanlarView(ListView):
#     model = Fanlar 
#     context_object_name="fanlar"
#     template_name=
def all(request):
    category_data=models.Fanlar.objects.all()
    return render(request,'blog/subject.html',{'data':category_data})
def index(request,test_id):
    fan=models.Fanlar.objects.get(id=test_id)
    questions=models.Test.objects.filter(fan=fan)

   
    return render(request,'blog/index.html',{'data':questions,'fan':fan})
    

# class FanView(ListView):
#     model = Fanlar
#     context_object_name = "fann"
#     template_name = "blog/subject.html"


class TestView(ListView):
    model = Test
    context_object_name = "javob"
    template_name = "blog/final.html"
    

def home(request):
    
    return render(request,"blog/home.html")
def final(request):
    
    return render(request,"blog/final.html")
def fan(request):
    
    return render(request,"blog/subject.html")