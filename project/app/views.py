from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

from .models import User

# Create your views here.

# def login(request):
#     global data
#     if request.method=='POST'  and (len(request.COOKIES)>1):
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         # print(request.COOKIES)
#         if request.COOKIES:
#             nameby=request.COOKIES['name']
#             emailby=request.COOKIES['email']
#             contactby=request.COOKIES['contact']
#             passwordby=request.COOKIES['password']

#             print(nameby,emailby,contactby,passwordby)

#             if emailby==email:
#                 if passwordby==password:
#                     data={
#                         'name':nameby,
#                         'email':emailby,
#                         'contact':contactby,
#                         'password':password
#                     }
#                     return render(request,'home.html',data)
#                 else:
#                     msg="Password Not Currect"
#                     return render(request,'login.html',{'msg':msg})
#             else:
#                 msg="Email Not Found"
#                 return render(request,'login.html',{'msg':msg})
#         else:
#             msg= "Please register first"
#             return render(request,'login.html',{'msg':msg})
#     else:
#         # msg= "Please register first"
#         return render(request,'login.html')
        

def registration(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            userData=User.objects.filter(user_email=email)
            print(userData)
            if userData:
                use_name=User.objects.filter(user_name=name)
                if use_name:
                    msg="Email ID and Name already exist"
                    return render(request, 'registration.html',{'msg':msg})
                else:
                    msg="Email id already exist please choose other 'email ID'"
                    return render(request, 'registration.html',{'msg':msg})
            else:
                User.objects.create(user_name=name,user_email=email,user_contact=contact,user_password=password)
                msg="Your Registration Successfull "
                return render(request,'registration.html',{'msg1':msg})
        else:
            msg="Password not match"
            return render (request,"registration.html",{'msg':msg})

    #=======================================================================================================   
        # user=Student.objects.get(stu_email=email)
        # Student.objects.create(stu_name=name,stu_email=email,stu_contact=contact,stu_password=password)
        # msg="DATA SUCCESSFULLY SUBMITED"
        # return render(request,'home.html',{'msg':msg})
    else:
        return render(request,'registration.html')


def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        print(email,password)
        use=User.objects.filter(user_email=email)
        print(use)
        if use:
            use_data=User.objects.get(user_email=email)
            print(use_data)
            email1=use_data.user_email
            name1=use_data.user_name
            contact1=use_data.user_contact 
            password1=use_data.user_password
            print(email1,name1,contact1,password1)
            if password1==password:
                data={
                    'nm':name1,
                    'em':email1,
                    'con':contact1,
                    'pas':password1
                }
                # all_query=Query.objects.filter(email=email1)
                return render(request,'index.html',{'data':data})
            else:
                msg="You Entered Incorrect Password"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="Email Id not Register"
            return render(request,'login.html',{'msg':msg})        
    else:
        return render(request,'login.html')



# def userData(request):
#     return render(request,'userData.html',data)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html' )

# def logout(request):
#     response=render(request,'userLogin.html')
#     response.delete_cookie('name')
#     response.delete_cookie('email')
#     response.delete_cookie('contact')
#     response.delete_cookie('password')
#     return response

def logout(request):
    return render(request,'login.html')

# def email(request):
#     return redirect("rlokhande06244@gmail.com")

def linkedin(request):
    return redirect("https://www.linkedin.com/in/rahul-lokhande-/")
def instagram(request):
    return redirect("https://www.instagram.com/")
def github(request):
    return redirect("https://github.com/rahullokhande123")