from django.shortcuts import render

from django.http import HttpResponse,JsonResponse


def index_view(request):
    return HttpResponse(render(request,'website/index.html'))


def about_view(request):
    return HttpResponse(render(request,'website/about.html'))

def contact_view(request):
    return HttpResponse(render(request,'website/contact.html'))