from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

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
                    return render(request,'home.html',data)
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