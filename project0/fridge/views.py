from django.shortcuts import render,redirect
# from . import modelscategory
# from . import modelsfridge
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    title = '冰箱管理'
    # fridge = modelsfridge.fridge()
    # fridges = fridge.all()
    return render(request,'fridge/index.html',locals())

def create(request):

    # if request.method =='POST' and request.FILES['fridgeimage']: #FILES須為大寫，後方的值須放在[]內
    #     myfile = request.FILES['fridgeimage']
    #     categoryid = request.POST['categoryid']
    #     modelnumber = request.POST['modelnumber']
    #     modelname = request.POST['modelname']
    #     unitcost = request.POST['unitcost']
    #     description = request.POST['description']
    #     myfile = request.FILES['fridgeimage']
    #     fridgeimage = myfile.name

    #     #新增資料
    #     fridge = modelsfridge.fridge()
    #     datas = tuple([categoryid,modelnumber,modelname,unitcost,fridgeimage,description])
    #     fridge.create(datas)

    #     #檔案上傳
    #     files1 = FileSystemStorage()
    #     files1.save(myfile.name,myfile) #fridgeimage.name得到的檔名指定給myfile

    #     return redirect("/fridge")#redirect需要import
    # category = modelscategory.Category()
    # datas = category.all()      
    # title = '商品新增'
    return render(request,'fridge/create.html',locals())
