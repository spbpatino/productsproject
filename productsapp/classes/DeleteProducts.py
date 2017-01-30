from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from productsapp.models import Products

class DeleteProducts(LoginRequiredMixin, TemplateView):
	login_url = '../../login/'
	redirect_field_name = 'products'
	model = Products

	def post(self, request, *args, **kwargs):
		print(str(request.POST['id']))
		product = Products.objects.filter(pk=request.POST['id'])
		product.delete()		
		return JsonResponse({'response':'OK'}, safe=False)