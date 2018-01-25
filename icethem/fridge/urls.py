from django.urls import path
from . import views
app_name='fridge'
urlpatterns = [
    path('',views.index,name='index'),#記得每行結尾用逗號,區隔!!#路由名/放在後端
    path('create',views.create,name='create'),
    path('update',views.update,name='update'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete ,name='delete'),
    path('stacks',views.stacks,name='stacks'),
    path('sort/<str:foodid>',views.sort ,name='sort'),

]