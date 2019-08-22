from django.shortcuts import render,redirect
from myapp.forms import UserForm,UserInfoForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from myapp.models import UserInfo
from django.contrib.auth.models import User



def login_view(request):
    if request.method == 'POST' and 'login_btn' in request.POST:
        login_username = request.POST.get('username')
        login_password = request.POST.get('password')

        user = authenticate(username = login_username, password = login_password)

        if user :
            if user.is_active:
                login(request,user)
                return redirect('myapp:home')
            else:
                messages.error(request,"This Id is Blocked!")
        else:
            messages.error(request,"Wrong username or password!")

    if request.method == 'POST' and 'reg_btn' in request.POST:
        form = UserForm( data= request.POST)
        if form.is_valid():
            userF = form.save()
            passworldofuser = userF.password
            userF.set_password(userF.password)
            userF.save()
            user = authenticate(username=userF.username,password= passworldofuser)
            if user:
                login(request,user)
            return redirect('myapp:complete_profile')

        else:
            messages.error(request,"username exists!")



    return render(request,'myapp/login.html',{'form':UserForm})


@login_required
def logout_view(request):
    logout(request)
    return redirect('myapp:login_page')

@login_required
def complete_profile_view(request):


    if request.method == 'POST':
        form = UserInfoForm(data = request.POST)
        if form.is_valid():

            info = form.save(commit=False)
            info.user_id = request.user.id

            if 'pic' in request.FILES:
                info.pic = request.FILES['pic']
            info.save()


            return redirect('myapp:home')
        else:
            print("Invalid Form")
            messages.error(request,"Fill Facebook/Instagram link Correctly.")
    return render(request,'myapp/complete_profile.html',{'form':UserInfoForm})

@login_required
def edit_profile_view(request):
    try:
        user_data = UserInfo.objects.get(user_id=request.user.id)
    except:
        return redirect("myapp:complete_profile")

    user_data2 = User.objects.get(id=request.user.id)

    form1 = UserForm(initial= {'username':user_data2.username,
                                'email':user_data2.email,
                               })

    form2 = UserInfoForm(initial= {'name':user_data.name,
                                   'cell':user_data.cell,
                                   'age':user_data.age,
                                   'gender':user_data.gender,
                                   'fb': user_data.fb,
                                   'insta': user_data.insta,
                                   'address': user_data.address,
                                   'city': user_data.city,
                                   'education_level': user_data.education_level,
                                   'education_field': user_data.education_field,
                                   'work_as': user_data.work_as,
                                   'work_in': user_data.work_in,
                                   'religion': user_data.religion,
                                   })
    if request.method == "POST":
        new_form1 = UserForm(data=request.POST)
        new_form2 = UserInfoForm(data=request.POST)


        if new_form2.is_valid():

            user_data2.email = request.POST.get('email')
            user_data2.set_password(request.POST.get('password'))
            user_data2.save()


            user_data.name = request.POST.get('name')
            user_data.cell = request.POST.get('cell')
            user_data.fb = request.POST.get('fb')
            user_data.insta = request.POST.get('insta')
            user_data.address = request.POST.get('address')
            user_data.city = request.POST.get('city')
            user_data.education_level = request.POST.get('education_level')
            user_data.education_field = request.POST.get('education_field')
            user_data.work_as = request.POST.get('work_as')
            user_data.work_in = request.POST.get('work_in')
            user_data.religion = request.POST.get('religion')
            if 'pic' in request.FILES:
                user_data.pic = request.FILES['pic']

            user_data.save()

            user = authenticate(username=request.POST.get('username'),password= request.POST.get('password'))
            if user:
                login(request,user)

        else:
            messages.error(request,"Fill Facebook link Correctly.")
        return redirect('myapp:edit_profile')


    return render(request,'myapp/edit_profile.html',{'form2':form2,'form1':form1,"pic":user_data.pic})




@login_required
def home(request):
    try:
        user_data = UserInfo.objects.get(user_id=request.user.id)
    except:
        messages.error(request,"Complete Your profile first.")
        return redirect("myapp:complete_profile")
    data = UserInfo.objects.all()
    return render(request,'myapp/home.html',{'pic':user_data.pic,'object':data,'gen':'all'})
def home_male(request):
    user_data = UserInfo.objects.get(user_id=request.user.id)
    data = UserInfo.objects.all()
    return render(request,'myapp/home.html',{'pic':user_data.pic,'object':data,'gen':'male'})
def home_female(request):
    user_data = UserInfo.objects.get(user_id=request.user.id)
    data = UserInfo.objects.all()
    return render(request,'myapp/home.html',{'pic':user_data.pic,'object':data,'gen':'female'})


@login_required
def profile(request,slugtxt):
    user_data = UserInfo.objects.get(slug=slugtxt)
    return render(request,'myapp/profile.html',{'person':user_data,"pic":user_data.pic})

@login_required
def deleteAc_view(request):
    user_name = request.user.username
    try:
        u = User.objects.get(username = user_name)
        n = UserInfo.objects.get(user = u)
        n.pic.delete()
        u.delete()
        messages.success(request, "Account deleted successfully!")
        return redirect("myapp:login_page")
    except:
        print('The user is not deleted')

    return redirect("myapp:edit_profile")
