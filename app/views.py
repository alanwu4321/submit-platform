from django.shortcuts import render
from app.models import User,Admin,UserFile
from app.forms import NewUserForm,NewUserFileForm
from django.views.generic.edit import FormView



# Create your views here.
def index(request):
    return render(request,'app/index.html')
def try1(request):
    user_list=UserFile.objects.all()
    user_dict={'try1':user_list}
    return render(request,'app/history.html',context=user_dict)
def history(request):
    user_list = UserFile.objects.order_by('id')
    user_dict={'users':user_list}
    return render(request, 'app/history.html',context=user_dict)

def historysortbyOtoNew(request):
    user_list = UserFile.objects.order_by('submission_Time')
    user_dict={'users':user_list} 
    return render(request, 'app/history.html',context=user_dict)

def historysortbyNewtoO(request):
    user_list = UserFile.objects.order_by('-submission_Time')
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
    fileform = NewUserFileForm()
    if request.method =='POST':
        file_form=NewUserFileForm(request.POST,request.FILES)
        files = request.FILES.getlist('submission_Box')
        form =NewUserForm(request.POST) #nOW the instance of the class will have the value
        if form.is_valid():
            form_instance=form.save(commit=False)
            form.save(commit=True)
            for f in files:
                file_instance = UserFile(submission_Box=f, group=form_instance)
                file_instance.save()
            return history(request)
        else: 
            return adminsubmit(request)
    return render(request,'app/user.html',{'form':form,'fileform':fileform})


