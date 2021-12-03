from django.urls import path
from .views import (
	image_like, image_list,
	image_detail, image_create,
	image_ranking)

# here must be the urls 
app_name = 'images'

urlpatterns = [
	path('detail/<int:id>/<slug:slug>/', image_detail, name='detail'),
	path('create/', image_create, name='create'),
	path('list/', image_list, name = 'list'),
	path('like/', image_like, name = 'like'),
	path('ranking/', image_ranking, name='create'),
	
]