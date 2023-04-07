# the core app, contains the views to the home page that's all that needs to be send to the template homepage
# 

from django.shortcuts import redirect, render
from item.models import *
from core.forms import SignupForm
# Create your views here.
# the veiws desplaye information to the home page that's any information to be displayer to the home page
def index(request):
    items = Item.objects.filter(is_sold = False)
    
    category = Category.objects.all()
    
    context = {
        'items':items,
        'category':category
    }
    
    return render(request , 'core/index.html', context)


def contact(request):
    
    return render(request , 'core/contact.html')


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request , 'core/signup.html', {'form':form,})