
from django.conf.urls import url,include
from django.urls import path
from .views import albums_view,albums_with_photo,album_update
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    path('add',views.add,name='add'),
    path('add_photo',views.add_photo,name='add_photo'),
    path('gallery',views.gallery,name = 'gallery'),
    path('photo_detail/<int:a_id>/', views.photo_detail),
    path('album_view', albums_view.as_view()),
    path('album_view/<int:pk>', albums_with_photo.as_view()),
    url(r'^update/(?P<pk>\d+)/$', album_update.as_view(), name='book_update'),
]
