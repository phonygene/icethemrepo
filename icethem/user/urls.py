from django.urls import path
from . import views
app_name='user'
urlpatterns = [
    path('', views.index,name='index'),
    path('create/', views.create,name='create'),
    path('update/<int:id>', views.update,name='update'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('checkname/<str:name>',views.checkname,name='checkname'),
    path('captcha/',views.captcha,name='captcha')
]