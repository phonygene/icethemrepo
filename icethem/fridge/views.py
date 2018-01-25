from django.shortcuts import render,redirect
from . import modelsfoods
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def index(request):
    title = '食物管理'
    food = modelsfoods.Foods()
    foodsall = food.all()
    print(foodsall)
    return render(request,'fridge/index.html',locals())

def create(request):
    if request.method == "POST" and request.FILES['foodimg']:
        foodname = request.POST['foodname']
        foodtype = request.POST['foodtype']
        iceddate = request.POST['iceddate']
        expiredate = request.POST['expiredate']
        description = request.POST['description']
        thefile = request.FILES['foodimg']
        foodimg = thefile.name

        #資料新增
        food = modelsfoods.Foods()
        datas = tuple([foodname,foodtype,iceddate,expiredate,foodimg,description])
        food.create(datas)

        #檔案上傳
        fs = FileSystemStorage()
        fs.save(thefile.name,thefile)
        
        return redirect("/fridge")

    foods = modelsfoods.Foods()
    datas = foods.all()

    title = "商品新增"
    return render(request,'fridge/create.html',locals())

def update(request, id):
    if request.method == "POST" and request.FILES['foodimg']:
        foodname = request.POST['foodname']
        foodtype = request.POST['foodtype']
        iceddate = request.POST['iceddate']
        expiredate = request.POST['expiredate']
        description = request.POST['description']
        thefile = request.FILES['foodimg']
        foodimg = thefile.name

        food = modelsfoods.Foods()
        datas = tuple([foodname,foodtype,iceddate,expiredate,foodimg,description])
        food.update(datas)

        #檔案上傳
        fs = FileSystemStorage()
        fs.save(thefile.name,thefile)
        
        return redirect("/product")

def delete(reqeust, id):
    food = modelsfoods.Foods()
    food.delete(id)
    return redirect("/fridge")

def fridge(request):
    title = 'fridge'

    return render(request,'fridge/fridge.html',locals())
def stacks(request):
    title = 'stacks'
    food = modelsfoods.Foods()
    foodsall = food.all()
    return render(request,'fridge/stacks.html',locals())
def sort(request,foodid):

    return HttpResponse("food:"+foodid)



