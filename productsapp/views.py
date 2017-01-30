from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate
from productsapp.models import PlatformUser

"""def login(request):
    
	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				#login(request, user)
				return HttpResponseRedirect(reverse('productsapp:products'))	
			else:
				return render(request, 'productsapp/login.html', {'location': {'here':'LOGIN'}})
		else:
			return render(request, 'productsapp/login.html', {'location': {'here':'LOGIN'}})

	else:
		print("hola no post")
		return render(request, 'productsapp/login.html', {'location': {'here':'LOGIN'}})
"""
