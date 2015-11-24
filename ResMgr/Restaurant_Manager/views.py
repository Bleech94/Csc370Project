from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse

from Restaurant_Manager.models import FoodItem

# Create your views here.

def index(request):
	dishes = FoodItem.objects.all()
	return render(request, 'Restaurant_Manager/index.html', {'dishes': dishes})
	
def account(request):
    return render(request, 'Restaurant_Manager/account.html')
