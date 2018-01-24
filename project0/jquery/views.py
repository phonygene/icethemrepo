from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from member.models import Member
from django.core import serializers
# Create your views here.
def index(request):
    title = "jquery app"
    return render(request,'jquery/index.html',locals())

def httpget(request):
    title = "http get"
    name = request.GET['name']
    age = request.GET['age']
    return HttpResponse('Hello {}, you are {} years old'.format(name,age))

def httppost(request):
    title = "http post"
    name = request.POST['name']
    age = request.POST['age']
    return HttpResponse('Hello {}, you are {} years old'.format(name,age))

def getjson(reqeust):
    members = Member.objects.all()
    datas = serializers.serialize('json', members)
    return JsonResponse(datas,safe=False) 

def getxml(request):
    data = serializers.serialize("xml", Member.objects.all(),fields=('username','useremail'))
    return HttpResponse(data,content_type='application/xml')

def todos(request):
    title = "todo app"
    return render(request,'jquery/todos.html',locals())