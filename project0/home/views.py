from django.shortcuts import render
from django.http import HttpResponse
import datetime

#檔案上傳用!!
from django.core.files.storage import FileSystemStorage

# def index(request):
#     return HttpResponse("<h2>index home</h2>")
def index(request):
    datas = [{'name':'Jason','age':30,'email':'jason@gmail.com'},
             {'name':'Tim','age':18,'email':'Tim@gmail.com'},
             {'name':'Howard','age':33,'email':'Howard@gmail.com'}]

    return render(request,'home/index.html',{'title':'首頁(由index function傳來)','users':datas,'name':'jason','now':datetime.datetime.now()})
    # return render(request,'home/index.html',{'title':'首頁'})
def about(request):
    # return HttpResponse("<h2>Home About</h2>")
    title = 'about'
    if request.method == 'POST':
        email = request.POST['useremail']
        name = request.POST['username']
    return render(request,'home/about.html',locals())
def contact(request):
    title = 'contactus'
    if 'name' in request.GET: #if 'name'需加引號表示為name屬性而不是變數
        name = request.GET['name']
    else:
        name = 'guest'
    if 'id' in request.GET:
        userid = request.GET['id']
    else:
        userid = '0000'
    return render(request,'home/contact.html',locals())
def service(request):
    title = 'service'
    return render(request,'home/service.html',locals())
def contact1(request,name):
    title = 'contact'

    title="聯絡 " + name
    return render(request,'home/contact1.html',locals())
def upload(request):
    if request.method =='POST' and request.FILES['myfile']: #FILES須為大寫，後方的值須放在[]內
        myfile = request.FILES['myfile']
        files1 = FileSystemStorage()
        files1.save(myfile.name,myfile) #將myfile.name得到的檔名指定給myfile
    title = '檔案上傳'
    return render(request,'home/uploadfiles.html',locals())




    
# Create your views here.
