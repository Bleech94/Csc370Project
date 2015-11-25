from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from django.db.models import Q

from .models import Order
from .models import Receipt
from .models import FoodItem

# Create your views here.

def index(request):
	dishes = FoodItem.objects.all()
	error = ""
	
	action = request.GET.get('action', '0')
	if(action != 0):
		if(action == "addCustomer"):
			customers = int(request.GET.get('customers', '0'))
			table = int(request.GET.get('table', '0'))
			if(customers > 0 and customers < 5 and table > 0 and table < 7):
				error = "Adding "+str(customers)+" customers to table "+str(table)+"."
				customer = []
				for x in range(customers):
					customer.append(Receipt(table = table))
					customer[x].save()
			
		elif(action == "addDish"):
			#Retrieve request parameters
			customer = int(request.GET.get('customer', '0'))
			table = int(request.GET.get('table', '0'))
			dish = request.GET.get('dish', '0')
			# Check if values are valid
			if(customer > 0 and customer < 5 and table > 0 and table < 7 and dish != 0):
				# Set messagebox
				error = "Adding "+dish+" to customer "+str(customer)+" at table "+str(table)+"."
				# Get id of customer at 'customer'th seat, at 'table' table
				customerID = Receipt.objects.filter(table = table)[customer-1].number
				# Save the order
				newOrder = Order(customer = customerID, foodItem = dish)
				newOrder.save()
			
		elif(action == "emptyTable"):
			#Retreive the request parameters
			table = int(request.GET.get('table', '0'))
			payee = int(request.GET.get('payee', '0'))
			error = "Clearing out table "+str(table)+" and creating receipts."
			
			if(table > 0 and table < 7 and payee > -1 and payee < 5):
				if(payee == 0):
					# Individual bills
					customersList = Receipt.objects.filter(table = table)[:4]
					for c in customersList:
						# Calculate totals
						orders = Order.objects.filter(customer = c.number)
						costSum = 0
						ingSum = 0
						for o in orders:
							f = FoodItem.objects.get(pk = o.foodItem)
							costSum += f.customer_price
							ingSum += f.ingredient_price
						# Update the customer
						cust = Receipt.objects.get(pk = c.number)
						cust.table = -1
						cust.customer_total = costSum
						cust.ingredient_total = ingSum
						cust.save()
				else:
					# Someone is paying it all
					pass
	
	
	
	# This should be in a loop with an array but yoloswag
	t1 = Receipt.objects.filter(table = 1)
	t2 = Receipt.objects.filter(table = 2)
	t3 = Receipt.objects.filter(table = 3)
	t4 = Receipt.objects.filter(table = 4)
	t5 = Receipt.objects.filter(table = 5)
	t6 = Receipt.objects.filter(table = 6)
	# Create a list of orders at a table
	t1Receipts, t2Receipts, t3Receipts, t4Receipts, t5Receipts, t6Receipts = [], [], [], [], [], [] 
	for c in t1:
		t1Receipts.append(c.number)
	for c in t2:
		t2Receipts.append(c.number)
	for c in t3:
		t3Receipts.append(c.number)
	for c in t4:
		t4Receipts.append(c.number)
	for c in t5:
		t5Receipts.append(c.number)
	for c in t6:
		t6Receipts.append(c.number)
	t1Orders = Order.objects.filter(customer__in=t1Receipts)
	t2Orders = Order.objects.filter(customer__in=t2Receipts)
	t3Orders = Order.objects.filter(customer__in=t3Receipts)
	t4Orders = Order.objects.filter(customer__in=t4Receipts)
	t5Orders = Order.objects.filter(customer__in=t5Receipts)
	t6Orders = Order.objects.filter(customer__in=t6Receipts)
	return render(request, 'Restaurant_Manager/index.html', {'dishes': dishes, 'error': error, 't1':t1, 't2':t2, 't3':t3, 't4':t4, 't5':t5, 't6':t6, 't1Orders': t1Orders,'t2Orders': t2Orders,'t3Orders': t3Orders,'t4Orders': t4Orders,'t5Orders': t5Orders,'t6Orders': t6Orders})
	
	
def account(request):
    return render(request, 'Restaurant_Manager/account.html')
