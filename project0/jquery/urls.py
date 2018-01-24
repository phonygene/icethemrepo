from django.urls import path
from . import views
app_name='jquery'
urlpatterns = [
    path('', views.index,name='index'),  
    path('httpget', views.httpget,name='get'),  
    path('httppost', views.httppost,name='post'), 
    path('getjson', views.getjson,name='json'), 
    path('getxml', views.getxml,name='xml'), 
    path('todos',views.todos,name='todos')
]