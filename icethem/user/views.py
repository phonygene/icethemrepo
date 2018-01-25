from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from .models import User
from django.contrib.staticfiles import finders
# Create your views here.
def index(request):  
    
    title = "會員管理"

    #todo 讀取會員資料傳給index.html
    users = User.objects.all()
    # print(users)
    # name = request.COOKIES['name']
    return render(request,'user/index.html',locals())

def create(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        useremail = request.POST["useremail"]
        # userbirth = request.POST["userbirth"]

        #todo 接收到的會員資料寫進資料庫
        User.objects.create(username=username,useremail=useremail,password=password)
        
        #todo 新增完成後轉到http://localhost:8000/user
        return redirect("/user")
       
    title = "會員新增" 
    return render(request,'user/create.html',locals())

def update(request,id):
    if request.method == 'POST':        
        username = request.POST["username"]      
        useremail = request.POST["useremail"]


        #todo 修改資料庫中的會員資料
        user = User.objects.get(id=int(id))
        User.username = username
        User.useremail = useremail
        User.save()
        #todo 修改完成後轉到http://localhost:8000/user
        return redirect("/user")

    title = "會員修改"
    #todo 根據會員編號取得會員資料傳給update.html
    user = User.objects.get(id=int(id))

    return render(request,'user/update.html',locals())

def delete(request,id):
    #todo 根據會員編號刪除會員資料
    user = User.objects.get(id=int(id))
    user.delete()

    #todo 刪除完成後轉到http://localhost:8000/user
    return redirect('/user')

def login(request):   
    if request.method == "POST":
        email = request.POST['useremail']
        pwd = request.POST['userpassword']
        captcha = request.POST['captcha']
        if request.session['captcha'] == captcha:
            user = User.objects.filter(useremail=email,password=pwd).values('username')
        
            if user:
                theuser = user[0]            
                response = HttpResponse("<script>alert('登入成功');location.href='/user/'</script>")
                if 'reuserme' in request.POST.keys() and request.POST['reuserme']:
                    expiresdate = datetime.datetime.now() + datetime.timedelta(days=7)
                    response.set_cookie("name",theuser['username'],expires=expiresdate)
                else:
                    response.set_cookie("name",theuser['username'])
                return response
            else:
                return HttpResponse("<script>alert('登入失敗，密碼錯誤');location.href='/user/login'</script>")
        else:
            return HttpResponse("<script>alert('驗證碼輸入錯誤，請重新輸入');location.href='/user/login'</script>")
    title = "會員登入"
    return render(request,'user/login.html',locals())

def logout(request):
    response = HttpResponse("<script>alert('登出');location.href='/user/login'</script>")
    response.delete_cookie('name')
    return response

def checkname(request,name):
    # name = request.GET['name'];
    # 檢查name是否在資料庫中
    # SQL語法  select username where username='Jack'
    # ORM User.objects.filter(username=name)
    result = User.objects.filter(username=name)
    if result :
        message = "帳號已存在"
    else:
        message = "帳號不存在"
        
    return HttpResponse(message)

def captcha(request):    
    import random
    # 安裝 pillow  pip install pillow
    from PIL import Image,ImageDraw,ImageFont
    list1 = random.sample(['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'],5)
    txt = ''.join(list1)    
    
    # todo 將產生的數字及字母存到session中
    request.session['captcha'] = txt  
    
    width = 15 * 5
    height = 30
    image = Image.new('RGB', (width, height), (255, 255, 255))    
    # 下載字體https://fonts.google.com/
    thefont = finders.find('fonts/GiveYouGlory.ttf')
    font = ImageFont.truetype(thefont, 22)   
    draw = ImageDraw.Draw(image)
    draw.text((5, 5), txt,font=font, fill=(255, 0, 0))
    response = HttpResponse(content_type="image/png")
    image.save(response, "PNG")
    return response
