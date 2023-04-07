from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from item.forms import EditForm, NewForm
from django.contrib.auth.decorators import login_required
from item.models import Category, Item
from django.db.models import Q
# Create your views here.

# contains the information about the dettails page 
def items(request):
    query = request.GET.get('query')
    categor_id = request.GET.get('categor',0)
    
    items= Item.objects.filter(is_sold = False)
    category = Category.objects.all()
    if query:
        items= items.filter(Q(name__icontains = query)| Q(description__icontains = query))
    
    return render(request , 'item/items.html', {'items':items, 'query':query, 'category':category,'categor_id':int(categor_id)})




def detail(request , pk): # each item has a pk value 
    item = get_object_or_404(Item, pk=pk) # the Item meqans we are taking data from the models of the item app
    relate_item = Item.objects.filter(category = item.category , is_sold = False).exclude(pk = pk)[0:3]
    
    context = {
        'item':item,
        'relate_item':relate_item
    }
    
    return render(request , 'item/detail.html', context)




@login_required
def new(request):
    if request.method == "POST":
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk = item.id)
    else:
        form = NewForm()
    return render(request ,'item/form.html', {'form':form,'title':'New item'})




@login_required
def edit(request ,pk):
    item =get_object_or_404(Item, pk = pk , created_by = request.user)
    if request.method == "POST":
        form = EditForm(request.POST, request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk = item.id)
    else:
        form = EditForm(instance=item)
    return render(request ,'item/form.html', {'form':form,'title':'Edit item'})










@login_required
def delete(request , pk ):
    pk = int(pk)
    item =get_object_or_404(Item, pk=pk , created_by = request.user)
    item.delete()
    return redirect('deshboard:index')