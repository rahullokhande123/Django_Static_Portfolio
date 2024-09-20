from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def userLogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        nameby=request.COOKIES['name']
        emailby=request.COOKIES['email']
        contactby=request.COOKIES['contact']
        passwordby=request.COOKIES['password']

        print(nameby,emailby,contactby,passwordby)

        if emailby==email:
            if passwordby==password:
                data={
                    'name':name,
                    'email':email,
                    'contact':contact
                }
                return render(request,'base.html',data)
            else:
                msg="Password Not Currect"
                return render(request,'userLogin.html',{'msg':msg})
        else:
            msg="Email Not Found"
            return render(request,'userLogin.html',{'msg':msg})
    else:
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
    response.set_cookie('name',name)
    response.set_cookie('email',email)
    response.set_cookie('contact',contact)
    response.set_cookie('password',password)
    return response