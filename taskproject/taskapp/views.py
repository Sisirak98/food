from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from taskapp.models import branch, product, category, accoun


def home(request):
    br = branch.objects.all()
    return render(request,"home.html",{'branch':br})
def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('taskapp:allcat')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('taskapp:log')
    return render(request, "login.html")


def regis(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpass = request.POST['cpass']
        if password == cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('taskapp:regis')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('taskapp:regis')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                messages.info(request,"Registation successfull")
                return redirect('taskapp:log')

        else:
            messages.info(request, "Password and confirm password should be same.")
            return redirect('taskapp:regis')
    return render(request,"index.html")


def lout(request):
    auth.logout(request)
    return redirect('taskapp:home')


def allcat(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug != None:
        c_page=get_object_or_404(category,slug=c_slug)
        products_list=product.objects.all().filter(category=c_page,available=True)
    else:
        products_list=product.objects.all().filter(available=True)
    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(request,"cat.html",{'category':c_page,'products':products})

def prodetails(request,c_slug,pro_slug):
    try:
        pro=product.objects.get(category__slug=c_slug,slug=pro_slug)
    except Exception as e:
        raise e
    return render(request,"product.html",{'pro':pro})


def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        addr = request.POST['addr']
        phone = request.POST['phone']
        cart_item = accoun.objects.create(name=name, addr=addr, phone=phone)
        cart_item.save()
        messages.info(request, " successfully Added")
        return redirect('taskapp:home')
    return render(request,"address.html")