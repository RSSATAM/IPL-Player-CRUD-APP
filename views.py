from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login , logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def home_page(request):
    return render(request,'home.html')

def anchor(request):
    return render(request, 'anchor.html')




@login_required
def create(request):
    if request.method =='POST':
        j=request.POST.get('jn')
        p=request.POST.get('pn')
        r=request.POST.get('rl')
        t=request.POST.get('tn')

        obj=players(j,p,r,t)
        obj.save()
        return redirect('/display/')
    
    else:
        return render(request, 'create.html')
    
@login_required
def display(request):
    data=players.objects.all()
    context={'data':data}
    return render(request, 'display.html',context)

@login_required
def delete(request,jer):
    obj=players.objects.get(jer_no=jer)
    obj.delete()
    return redirect('/display/')


@login_required
def update(request,jer):
    
    if request.method =='POST':
        
        j=request.POST.get('jn')
        p=request.POST.get('pn')
        r=request.POST.get('rl')
        t=request.POST.get('tn')

        obj=players(j,p,r,t)
        obj.save()
        return redirect('/display/')
    
    else:
        obj=players.objects.get(jer_no=jer)
        context={'ob':obj}
        return render(request,'update.html',context)

    

# sirs approach ====disable jer no
# def update(request,jer):
#     obj=players.objects.get(jer_no=jer)
#     context={'ob':obj}
    
#     if request.method =='POST':
        
       
#         p=request.POST.get('pn')
#         r=request.POST.get('rl')
#         t=request.POST.get('tn')

#         obj.pname=p
#         obj.role=r
#         obj.team=t
#         obj.save()
#         return redirect('/display/')
    
#     else:
        
#         return render(request,'update.html',context)

    

def loginn(request):
    if request.method=='POST':
        u=request.POST.get('un')
        ps=request.POST.get('pas')
        
        user=authenticate(request,username=u, password=ps)

        if user is  None:
            return render(request,'loginn.html',{'err': 'Invalid credentials'})
        
        else:
            login(request,user)
            return redirect('/create/')
    
    else:
        return render(request, 'loginn.html')



    

def sign_up(request):

    if request.method=='POST':
        u=request.POST.get('un')
        ps=request.POST.get('pas')
        e=request.POST.get('mail')
        f=request.POST.get('ph')

        if User.objects.filter(username=u).exists():
            return render(request,'sign_up.html',{'err':'User already exists'})
       
        User.objects.create_user(username=u,password=ps,email=e)
    
        return redirect('/login/')

    else:

        return render(request, 'sign_up.html')
    

def logout1(request):
    logout(request)
    return redirect('/login/')

    

