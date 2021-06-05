
from django.conf.urls import url,include
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    path('add',views.add,name='add'),
    path('add_photo',views.add_photo,name='add_photo'),
    path('gallery',views.gallery,name = 'gallery'),
    path('photo_detail/<int:a_id>/', views.photo_detail),
]
