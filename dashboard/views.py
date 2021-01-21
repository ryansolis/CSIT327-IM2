from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import ProductForm
from .models import *

# Create your views here.
class DashboardCustomerView(View):
	def get(self,request):
		return render(request, 'customer.html')
class DashboardProductView(View):
	def get(self,request):
		dash_prod = Product.objects.all()
		context = {
			'products' : dash_prod
		}
		return render(request,'product.html', context)

	def post(self, request):
		if request.method == 'POST':	
			if 'btnUpdate' in request.POST:	
				print('update profile button clicked')
				pid = request.POST.get("prod-id")			
				ctgry = request.POST.get("prod-category")
				brnd = request.POST.get("prod-brand")
				pname = request.POST.get("prod-name")
				psize = request.POST.get("prod-size")
				pprice = request.POST.get("prod-price")
				pstocks = request.POST.get("prod-stocks")
				update_prod = Product.objects.filter(id = pid).update(category = ctgry, brand = brnd, name = pname, size = psize, price =pprice,
									  stocks = pstocks)
				print(update_prod)
				print('profile updated')
			elif 'btnDelete' in request.POST:	
				print('delete button clicked')
				pid = request.POST.get("pprod-id")
				prod = Product.objects.filter(id=pid).delete()
				print('recorded deleted')
			elif 'btnAdd' in request.POST:
				return redirect('dashboard:register_view')
		#return HttpResponse ('post')
		return redirect('dashboard:product_view')
		

class ProductRegistrationView(View):
	def get(self,request):
		return render(request, 'registerprod.html')
	def post(self, request):		
		form = ProductForm(request.POST)		
		# fname = request.POST.get("firstname")
		# print(fname)
		# lname = request.POST.get("lastname")
		# print(lname)
		if form.is_valid():
			
			form.save()

			#return HttpResponse('Product record saved!')			
			return render(request,'recorded.html')
			# except:
			# 	raise Http404
		else:
			print(form.errors)
			return HttpResponse('not valid')