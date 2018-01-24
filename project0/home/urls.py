from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('',views.index,name='thisindex'),
    path('about123/',views.about,name='aboutme'),
    path('contact/',views.contact,name='contactus'),
    path('service/',views.service,name='allservice'),#記得每行結尾用逗號,區隔!!
    path('upload/',views.upload,name='uploadfiles')#路由名/放在後端
]