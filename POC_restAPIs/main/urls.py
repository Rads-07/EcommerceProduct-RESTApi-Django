from django.urls import path
from . import views
from .views import products
urlpatterns = [
    
    path('', views.home, name = "home"),
    path('products/', views.products, name="products"),
    path('products/<str:pk_test>', views.getProductById, name = "productId"),
    path('createProduct/', views.createProduct, name="createProduct"),
    path('updateProduct/<str:pk>', views.updateProduct, name = "updateProduct"),
    path('deleteProduct/<str:pk>', views.deleteProduct, name = "deleteProduct"),

    #for practise purpose
    #path('', views.Home.as_view(), name = "home"),
    #path('products/', views.ProductList.as_view(), name="products"),
    #path('products/<str:pk>', views.ProductById.as_view(), name = "productId"),
    #path('createProduct/', views.CreateProduct.as_view(), name="createProduct"),
]

