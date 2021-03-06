from django.urls import path ,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('men',views.men,name='men'),
    path('kid',views.kid,name='kid'),
    path('add',views.add,name='add'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('contact',views.contact,name='contact'),
    path('order',views.order,name='order'),
    path('login',views.login,name='login'),
    path('clogout',views.clogout,name='clogout'),
    path('cpassword',views.cpassword,name='cpassword'),
    path('cotp',views.cotp,name='cotp'),
    path('registration',views.registration,name='registration'),
    path('product',views.product,name='product'),
    path('women',views.women,name='women'),
]