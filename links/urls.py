from django.urls import path 
from .views import add_link,index , root_link 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , index , name='home'), 
    path('<str:link_slug>/' , root_link , name='root-link'),
    path('link/create' ,add_link , name='create-link' )
    
]
