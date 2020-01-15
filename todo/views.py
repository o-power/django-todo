from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello World")

def get_todo_list(request):
    results = Item.objects.all()
    return render(request, "todo_list.html", {'items': results})

def create_an_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm()

        #new_item = Item()
        #new_item.name = request.POST.get('name')
        #new_item.done = 'done' in request.POST
        #new_item.save()
        #return redirect(get_todo_list)
    
    return render(request, "item_form.html", {'form': form})

def edit_an_item(request, id):
    # Lookup by a primary key is the most common case, so Django provides a
    # shortcut for primary-key exact lookups.
    # Question.objects.get(pk=1) is identical to Question.objects.get(id=1).
    item = get_object_or_404(Item, pk=id)
    
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm(instance=item)

    # Load the template called item_form.html and passes it a context.
    # The context is a dictionary mapping template variable names to Python objects.
    context = {'form': form}
    return render(request, "item_form.html", context)

def toggle_status(request, id):
    item = get_object_or_404(Item, pk=id)
    item.done = not item.done
    item.save()

    return redirect(get_todo_list)