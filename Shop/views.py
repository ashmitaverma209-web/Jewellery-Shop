
from django.shortcuts import render, HttpResponse

from.models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        #print(name,email,phone,message)

        c=Contact(name=name,email=email,phone=phone,message=message)
        c.save()
    data=Contact.objects.all()
    return render(request,'contact.html',{"data":data})  
def home(request):
        return render(request,'home.html')    
def pricing(request):
    products = [
        
        {'name': 'Diamond Ring', 'price': 70000, 'image': 'yrg23022_1__3.png'},
        {'name': 'Diamond earrings', 'price': 50000, 'image': 'earrings.jpg'},
        {'name': 'Ring', 'price': 30000, 'image': 'yrg23022_3.jpg'},
        {'name': 'Necklace', 'price': 99000, 'image': 'necklace.jpg'},

        {'name': 'Bracelet', 'price': 120000, 'image': 'brace.jpg'},

    ]
    return render(request, 'pricing.html', {'products': products})

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')   # home page
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})


    return render(request,'login.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('login')   # (login page baad me bana sakte ho)

    return render(request, 'signup.html')

def collection(request):
    items = [
        {'name': 'Diamond Ring', 'price': 70000, 'image': 'yrg23022_1__3.png'},
        {'name': 'Necklace', 'price': 99000, 'image': 'necklace.jpg'},
        {'name': 'Brace', 'price': 120000, 'image': 'brace.jpg'},
        {'name': 'Earrings', 'price': 57000, 'image': 'earrings.jpg'},
        {'name': 'Diamond Ring', 'price': 70000, 'image': 'yrg23022_3.jpg'},
        {'name': 'Ring', 'price': 79000, 'image': 'images3.jpg'},
        {'name': 'necklace', 'price': 69000, 'image': 'OIP.jpg'},

             
    ]
    return render(request, 'collection.html', {'items': items})

def shop(request):
    products = [
        {'name': 'Diamond Ring', 'price': 70000, 'image': 'yrg23022_1__3.png'},
        {'name': 'Diamond earrings', 'price': 50000, 'image': 'earrings.jpg'},
        {'name': 'Ring', 'price': 30000, 'image': 'yrg23022_3.jpg'},
        {'name': 'Necklace', 'price': 99000, 'image': 'necklace.jpg'},

        {'name': 'Bracelet', 'price': 120000, 'image': 'brace.jpg'},

    ]
    return render(request, 'shop.html', {'products': products})

def collaboration(request):
    return render(request,'collaboration.html')    

def about(request):
    return render(request,'about.html')    