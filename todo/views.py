from django.shortcuts import render, HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello World")

def get_todo_list(request):
    return render(request, "todo_list.html")