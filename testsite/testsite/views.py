from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from django.core import serializers

from testsite.models import ToDoList

data = serializers.serialize("python",ToDoList.objects.all())

context = {
    'data' : data,
}

def ok(request):
    return render(request,'index.htm',context)