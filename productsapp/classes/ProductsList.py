from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.utils import timezone
import datetime

from productsapp.models import Products




class ProductsList(LoginRequiredMixin,ListView):
	login_url = '../../login/'
	redirect_field_name = 'products'
	model = Products
	template_name = 'productsapp/products.html'
	context_object_name = 'products_list'

	def get_context_data(self, **kwargs):
		context = super(ProductsList, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		context['location'] = {'here':'PRODUCTS'}
		return context
