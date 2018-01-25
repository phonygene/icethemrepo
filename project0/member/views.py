from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from .models import Member
from django.contrib.staticfiles import finders

# Create your views here.
def index(request):  
    
    title = "會員管理"
    members = Member.objects.all()
    #todo 讀取會員資料傳給index.html
    
    return render(request,'member/index.html',locals())

def create(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        useremail = request.POST["useremail"]
        userbirth = request.POST["userbirth"]

        #todo 接收到的會員資料寫進資料庫
        Member.objects.create(username=username,password=password,useremail=useremail,userbirth=userbirth)
        #todo 新增完成後轉到http://localhost:8000/member
        return redirect("/member")
    title = "會員新增" 
    return render(request,'member/create.html',locals())

def update(request,id):
    if request.method == 'POST':        
        username = request.POST["username"]      
        useremail = request.POST["useremail"]
        userbirth = request.POST["userbirth"]

        #todo 修改資料庫中的會員資料
        member = Member.objects.get(id=int(id))
        member.username = username
        member.useremail = useremail
        member.userbirth = userbirth
        member.save()
        #todo 修改完成後轉到http://localhost:8000/member
        return redirect("/member")

    title = "會員修改"
    #todo 根據會員編號取得會員資料傳給update.html
    #再拿一次，這次拿剛剛修改過的資料。傳給update.html
    member = Member.objects.get(id=int(id))
    
    return render(request,'member/update.html',locals())

def delete(request,id):
    #todo 根據會員編號刪除會員資料
    member = Member.objects.get(id=int(id))
    member.delete()
    #todo 刪除完成後轉到http://localhost:8000/member
    return redirect('/member')

def login(request):
    if request.method == "POST":
        email = request.POST['useremail']
        pwd = request.POST['userpassword']
        captcha = request.POST['captcha']
        if request.session['captcha'] == captcha:
            member = Member.objects.filter(useremail=email,password=pwd).values('username')

            if member:
                themember = member[0]
                response = HttpResponse("<script>alert('yes!');location.href='/member/'</script>")
                if 'rememberme' in request.POST.keys() and request.POST['rememberme']:
                    expiresdate = datetime.datetime.now() and datetime.timedelta(days=7)
                    response.set_cookie("name",themember['username'],expires=expiresdate)
                else:
                    response.set_cookie("name",themember['username'])
                    return response
            else:
                return HttpResponse("<script>alert('登入失敗，密碼錯誤！');location.href='/member/login'</script>")
        else:
            return HttpResponse("<script>alert('驗證碼輸入錯誤，請重新輸入');location.href='/member/login'</script>")
    title = "會員登入"
    return render(request,'member/login.html',locals())

def logout(request):
    response = HttpResponse("<script>alert('已登出');location.href='/member/login'</script>")
    response.delete_cookie('name')
   
    return response
def checkname(request,name):
    # name = request.GET['name'];
    # 檢查name是否在資料庫中
    # SQL語法  select username where username='Jack'
    # ORM Member.objects.filter(username=name)
    result = Member.objects.filter(username=name)
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
    
    width = 15 * 4
    height = 35
    image = Image.new('RGB', (width, height), (255, 255, 255))    
    # 下載字體https://fonts.google.com/
    thefont = finders.find('fonts/Kavivanar-Regular.ttf')
    font = ImageFont.truetype(thefont, 16)   
    draw = ImageDraw.Draw(image)
    draw.text((5, 5), txt,font=font, fill=(255, 0, 0))
    response = HttpResponse(content_type="image/png")
    image.save(response, "PNG")
    return response

