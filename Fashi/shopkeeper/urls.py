from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.logout, name='logout'),
    url(r'^index$', views.index, name='index'),
    url(r'^search$', views.search_item, name='search'),
    url(r'^women$', views.Women, name='women'),
    url(r'^Products/(?P<type>\w+)/(?P<name>\w+)/$', views.category, name='category'),
    url(r'^men$', views.Men, name='men'),
    url(r'^products$', views.Products, name='products'),
    url(r'^account$', views.Account, name='account'),
    url(r'^register$', views.Register_page, name='register'),
    url(r'^form/$', views.loginSubmit, name='loginSubmit'),
    url(r'^submit/$', views.registerSubmit, name='submit'),
    url(r'^contact$', views.Contact_page, name='contact'),
    url(r'^contactsubmit$', views.Contactsubmit, name='contactsubmit'),
    url(r'^single/(?P<id>\d+)/$', views.Single_product, name='single'),
    url(r'^add/(?P<id>\d+)/$', views.add_to_cart, name='add'),
    url(r'^delete/(?P<id>\d+)/$', views.delete_from_cart, name='delete'),
    url(r'^deleteproduct/(?P<id>\d+)/$', views.delete_product, name='deleteproduct'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^showcart$', views.showcart, name='showcart'),
]