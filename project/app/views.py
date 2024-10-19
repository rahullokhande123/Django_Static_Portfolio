from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def userLogin(request):
    global data
    if request.method=='POST'  and (len(request.COOKIES)>1):
        email=request.POST.get('email')
        password=request.POST.get('password')
        # print(request.COOKIES)
        if request.COOKIES:
            nameby=request.COOKIES['name']
            emailby=request.COOKIES['email']
            contactby=request.COOKIES['contact']
            passwordby=request.COOKIES['password']

            print(nameby,emailby,contactby,passwordby)

            if emailby==email:
                if passwordby==password:
                    data={
                        'name':nameby,
                        'email':emailby,
                        'contact':contactby,
                        'password':password
                    }
                    return render(request,'index.html',data)
                else:
                    msg="Password Not Currect"
                    return render(request,'userLogin.html',{'msg':msg})
            else:
                msg="Email Not Found"
                return render(request,'userLogin.html',{'msg':msg})
        else:
            msg= "Please register first"
            return render(request,'userLogin.html',{'msg':msg})
    else:
        # msg= "Please register first"
        return render(request,'userLogin.html')
        

def registration(request):
    return render(request,'registration.html')

def registerdata(request):
    print(request.method)
    print(request.POST)

    cstoken=request.POST.get('csrfmiddlewaretoken')
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    password=request.POST.get('password')

    response=render(request,'userLogin.html')
    response.set_cookie('name',name,max_age=365*24*60*60)
    response.set_cookie('email',email,max_age=365*24*60*60)
    response.set_cookie('contact',contact,max_age=365*24*60*60)
    response.set_cookie('password',password,max_age=365*24*60*60)
    return response
# def userData(request):
#     return render(request,'userData.html',data)
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request, 'contact.html' )
def logout(request):
    response=render(request,'userLogin.html')
    response.delete_cookie('name')
    response.delete_cookie('email')
    response.delete_cookie('contact')
    response.delete_cookie('password')
    return response

def linkedin(request):
    return redirect("https://www.linkedin.com/in/rahul-lokhande-/")
def instagram(request):
    return redirect("https://www.instagram.com/")
def github(request):
    return redirect("https://github.com/rahullokhande123")