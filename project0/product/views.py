from django.shortcuts import render,redirect
from . import modelscategory
from . import modelsproduct
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    title = '商品管理'
    product = modelsproduct.Product()
    products = product.all()
    return render(request,'product/index.html',locals())

def create(request):

    if request.method =='POST' and request.FILES['productimage']: #FILES須為大寫，後方的值須放在[]內
        myfile = request.FILES['productimage']
        categoryid = request.POST['categoryid']
        modelnumber = request.POST['modelnumber']
        modelname = request.POST['modelname']
        unitcost = request.POST['unitcost']
        description = request.POST['description']
        myfile = request.FILES['productimage']
        productimage = myfile.name

        #新增資料
        product = modelsproduct.Product()
        datas = tuple([categoryid,modelnumber,modelname,unitcost,productimage,description])
        product.create(datas)

        #檔案上傳
        files1 = FileSystemStorage()
        files1.save(myfile.name,myfile) #productimage.name得到的檔名指定給myfile

        return redirect("/product")#redirect需要import
    category = modelscategory.Category()
    datas = category.all()      
    title = '商品新增'
    return render(request,'product/create.html',locals())

def update(request, id):
    title = '商品修改'
    category = modelscategory.Category()
    categories = category.all()

    product = modelsproduct.Product()
    singleproduct = product.single(id)

    return render(request,'product/update.html',locals())

def delete(request, id):
    product = modelsproduct.Product()
    product.delete(id)
    return redirect("/product")
