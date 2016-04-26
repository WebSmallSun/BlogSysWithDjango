from django.shortcuts import render
from django.template import Template
from django.http import HttpResponse

def Home(request):
    #index = Template("IndexBase.html")
    return HttpResponse(render(request, "IndexBase.html"))
