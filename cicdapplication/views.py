from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hey hello I am there")