from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView
import datetime

from productsapp.models import Products


class CreateProducts(LoginRequiredMixin, TemplateView):
	login_url = '../../login/'
	redirect_field_name = 'products'
	model = Products

	def post(self, request, *args, **kwargs):
		print(self.request.user)
		now = datetime.datetime.now()
		new_product = Products(product_name = request.POST['product_name'], product_description = request.POST['product_description'], 
								product_tags = request.POST['product_tags'], creation_date = now.strftime("%Y-%m-%d %H:%M:%S"), user = self.request.user)
		new_product.save()		
		print(new_product.product_name)
		tags_list = new_product.product_tags.split(',')
		print(tags_list)
		products = [Products.objects.filter(product_tags__contains=tag) for tag in tags_list]
		response = serializers.serialize('json', products[0], fields=('product_name','product_description', 'product_tags', 'creation_date'))
		return JsonResponse(response, safe=False)