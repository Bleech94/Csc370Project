from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'Restaurant_Manager/index.html')

def account(request):
    return render(request, 'Restaurant_Manager/account.html')