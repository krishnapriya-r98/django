from django.shortcuts import render, redirect, get_object_or_404  
from users.forms import UserForm  
from users.models import users


def user(request):  
    if request.method == "POST":  
        form = UserForm(request.POST) 
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = UserForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    user_ = users.objects.all()  
    return render(request,"show.html",{'users':user_})

def edit(request, id):  
    user_ = users.objects.get(id=id)
    return render(request, 'edit.html', {'users':user_})  

def update(request, id):
    user_ = users.objects.get(id=id) 
    form = UserForm(request.POST, instance=user_)
    if form.is_valid():
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'users': user_})

def destroy(request, id):  
    user_ = users.objects.get(id=id)
    user_.delete()  
    return redirect("/show")  