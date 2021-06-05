from PIL import Image
from django.shortcuts import render
from django.http import HttpResponse
from .models import album,photo
import requests  
import json
from multiprocessing import Pool 
import threading
from concurrent.futures import ThreadPoolExecutor, Future


def index(request):
       albums = album.objects.all()
       return render(request, "index.html",{'albums':albums})      

def add(request):
       album.objects.all().delete()
       url = 'http://jsonplaceholder.typicode.com/albums' 
       response = requests.get(url)
       data = jsonRes = response.json() 
       for x in data :
              tom = album.objects.create(title=x['title'],userId = x['userId'])



def  download_image(image_url,id,alb,tit,thum):
    url = str(image_url)
    r = requests.get(url, allow_redirects=True)
    filename = url.split('/')[-1]
    pat = 'images/{}.png'.format(id)
    open(pat, 'wb').write(r.content)
    img = Image.open(pat)
    resized_img = img.resize((500, 500), Image.ANTIALIAS)
    resized_img.save(pat)
    tom = photo.objects.create(title=tit,id1 =id , albumId = alb , thumbnailUrl= thum,path =pat)


def add_photo(request):
       url = 'http://jsonplaceholder.typicode.com/photos' 
       response = requests.get(url)
       photo.objects.all().delete()
       data = jsonRes = response.json() 
       i = 0
       with ThreadPoolExecutor(max_workers=10) as executor:
              for x in data :
                     i +=1
                     executor.submit(download_image,x['url'],x['id'],x['albumId'],x['title'],x['thumbnailUrl'])
                     print(i)


def gallery(request):
       albums = album.objects.all()
       return render(request, "gl.html",{'albums':albums})      



def photo_detail(request, a_id):
       photos = photo.objects.filter(albumId = a_id)
       return render(request, "photo.html",{'photos':photos})     