from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import District,City,Person
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonCreationForm
from .models import Person, City
# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('credentials:register')

            else:
                user=User.objects.create_user(username=username,password=password)

                user.save();
            print("user created")
        else:
            messages.info(request,"password incorrect")
            return redirect('credentials:register')
        return redirect('credentials:login')
    return render(request,'register.html')



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('credentials:newpage')

        else:
            messages.info(request,"invalid Credentials")
            return redirect('credentials:login')

    return render(request,'login.html')


def newpage(request):
    return render(request,'newpage.html')

def logout(request):
    return render(request,'logout.html')

def application(request):
    return render(request,'application.html')








def person_create_view(request):

    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('credentials:application')
    return render(request, 'form.html', {'form': form})

#
def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('credentials:application', pk=pk)
    return render(request, 'form.html', {'form': form})


def load_cities(request):
    district_id = request.GET.get('district_id')
    cities = City.objects.filter(district_id=district_id).all()
    return render(request, 'city_dropdown_list.html', {'cities': cities})
