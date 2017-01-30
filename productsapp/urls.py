from django.conf.urls import url
from django.contrib.auth.views import logout_then_login
from productsapp.classes.ProductsList import ProductsList
from productsapp.classes.CreateProducts import CreateProducts
from productsapp.classes.DeleteProducts import DeleteProducts


app_name = 'productsapp'
urlpatterns = [
    url(r'^products/', ProductsList.as_view(), name='products'),
    url(r'^create/$', CreateProducts.as_view()),
    url(r'^delete/$', DeleteProducts.as_view()),
    url(r'^logout/$', logout_then_login),
] 