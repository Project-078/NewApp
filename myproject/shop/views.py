from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

def login(request):
    products = Product.objects.all()
    return render(request, 'shop/login.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/category_list.html', {'categories': categories})

def register(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request,'shop/register.html',{'form':form})
