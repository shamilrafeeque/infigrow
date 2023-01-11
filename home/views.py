from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm,UserForm
from .models import Account
from django.shortcuts import get_object_or_404,redirect, render
from django.contrib import messages,auth
from django.contrib.auth import logout
from django.http import JsonResponse

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            password = form.cleaned_data['password']
        
            
            user = Account.objects.create_user(username=username, email=email,password=password)
            user.mobile = mobile
            user.save()
            return redirect("login")
        else:
            error_message = form.errors
            return render(request, 'register.html', {'form': form, 'error': error_message})
         
    else:     
         form = RegistrationForm()
    context ={
        'form':form,
    }
    return render(request,'register.html',context)  


def login(request):
        if request.method=="POST":
            email = request.POST['email']
            password = request.POST['password']
            #print(email,password)
            user=auth.authenticate(request,email=email,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('index')
            else:
                messages.error(request,'invalid login credentials.')    
                return redirect('login')
        return render(request,'login.html')
  
    
    
    
def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')




def update_profile(request,pk):
    user = get_object_or_404(Account, id=pk)
    if request.method == 'POST':
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm(instance=request.user)
        pass
    return render(request, 'update_user.html', {'form': form})


def delete_account(request):
    user = request.user
    print(user)
    if request.method == 'POST':
        user.delete()
        return redirect('logout')
    else:
        return render(request, 'delete_account.html')
    

  
def user_logout(request):
    logout(request)
    messages.success(request, 'you are logged out.')
    return redirect("home")


def check_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': Account.objects.filter(email=email).exists()
    }
    return JsonResponse(data)