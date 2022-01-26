from os import name
from products.models import Service
from django.urls import path
from .import views
urlpatterns = [

    path('waters', views.waterSamples, name='waters'),
    #path('services', views.waterServices, name="services"),
    path('products', views.waterProducts, name='products'),
    path('product/<int:pk>/', views.productDetail, name='product'),
    path('fun', views.funAndGames, name='fun'),
    path('help', views.help, name='help'),
    path('about_us', views.aboutUs, name='about_us'),
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('cart', views.userCart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('update/', views.updateItem, name='update'),
    path('payment', views.paymentmethods, name='payment'),
    path('processOrder/', views.processOrder, name='processOrder'),
    path('brands', views.brands, name='brands'),
    path('service', views.Services, name='service'),
    path('mywater', views.mywater, name='mywater'),

    #News/ Blog
    path('welfare', views.NewsWelfare, name='welfare'),
    path('local', views.NewsLocal, name='local'),
    path('international', views.NewsInternational, name='international'),
    path('wallpapers', views.wallpapers, name='wallpapers'),
    path('waterfacts', views.waterfacts, name='waterfacts'),
    path('ringofwater', views.ringsofwater, name='ringofwater'),

    #path('num', views.getNumber, name='num'),
    # ADMIN

    path('addProduct', views.addProduct, name='addProduct'),
    path('modifyAllProduct', views.showProduct, name='modifyAllProduct'),
    path('updateProduct/<int:pk>', views.updateProduct, name='updateProduct'),
    path('deleteProduct/<int:pk>', views.deleteProduct, name='deleteProduct'),
    path('modifySingleProduct/<int:pk>',
         views.modifySingleProduct, name='modifySingleProduct'),
    path('addCategory',
         views.addCategory, name='addCategory'),
    path('addBrand',
         views.addBrand, name='addBrand'),
    path('createOrder', views.creteOrder, name='createOrder'),
    path('updateOrder/<str:pk>/', views.updateOrder, name='updateOrder'),
    path('deleteOrder/<str:pk>/', views.deleteOrder, name='deleteOrder'),
    path('serviceOrder', views.AdminService, name='serviceOrder')
]
