from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect
import datetime

# CRUD Operations

def create_view(request):
    
    if request.method == "POST":
        data    = request.POST.get("entry")
        author  = request.POST.get("author")

        print(data,author)

        models.ToDo(description = data, author = author).save()

        return HttpResponseRedirect('/show/')

def update_view(request,entry_id):

    if request.method == "POST":

        key    = request.POST.get("pk")
        author = request.POST.get("author")
        data   = request.POST.get("des")

        print(int(key),type(key),author,data) 
        
        try:
            row = models.ToDo.objects.get(pk = int(key))
            row.description = data
            row.author = author
            row.pub = datetime.datetime.now()

            row.save(update_fields=['description','author','pub'])

        except Exception as e:
            print("error",e)

        return HttpResponseRedirect('/show/')
    

def delete_view(request,entry_id):
    
    if request.method == "POST":
        try:
            row = models.ToDo.objects.get(pk = int(entry_id))
            row.delete()
        except Exception as e:
            print("error",e)

        return HttpResponseRedirect('/show/')

def show_view(request):
    return render(request,"index.html",{"tasks":models.ToDo.objects.all()})