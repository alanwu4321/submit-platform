from django.shortcuts import render
from app.models import User,Admin
from app.forms import NewUserForm


# Create your views here.
def index(request):
    return render(request,'app/index.html')
def history(request):
    user_list = User.objects.order_by('id')
    user_dict={'users':user_list}
    return render(request, 'app/history.html',context=user_dict)

def historysortbyOtoNew(request):
    user_list = User.objects.order_by('submission_Time')
    user_dict={'users':user_list} 
    return render(request, 'app/history.html',context=user_dict)

def historysortbyNewtoO(request):
    user_list = User.objects.order_by('-submission_Time')
    user_dict={'users':user_list} 
    return render(request, 'app/history.html',context=user_dict)



def adminsubmit(request):
    admin_list = Admin.objects.order_by('Project_Name')
    admin_dict={'admin':admin_list} 
    return render(request, 'app/index.html',context=admin_dict)

def userssortbyOtoNew(request):
    admin_list = Admin.objects.order_by('Project_DueDate')
    admin_dict={'admin':admin_list} 
    return render(request, 'app/index.html',context=admin_dict)
def userssortbyNewtoO(request):
    admin_list = Admin.objects.order_by('-Project_DueDate')
    admin_dict={'admin':admin_list} 
    return render(request, 'app/index.html',context=admin_dict)
    
def userssubmit(request):
    form = NewUserForm()

    if request.method =='POST':
        form =NewUserForm(request.POST, request.FILES) #nOW the instance of the class will have the value
        if form.is_valid():
            form.save(commit=True)
            return history(request)
        else: 
            return adminsubmit(request)
    return render(request,'app/user.html',{'form':form})

