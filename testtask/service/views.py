from django.shortcuts import render
from django.http import HttpResponse
from .models import album
import requests  
import requests
import json

def index(request):
       albums = album.objects.all() 
       return render(request, "index.html",{'albums':albums})      

def add(request):
       url = 'http://jsonplaceholder.typicode.com/albums' 
       response = requests.get(url)
       data = jsonRes = response.json() 
       for x in data :
              tom = album.objects.create(title=x['title'],userId = x['userId'])
