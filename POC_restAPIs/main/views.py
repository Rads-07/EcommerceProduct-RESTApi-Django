from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

# Create your views here.
@api_view(['GET'])
def home(request):
    api_urls = {
        'products':'api/products',
        'productById':'api/products/<str:pk_test>',
        'createProduct':'api/createProduct',
        'updateProduct':'api/updateProduct/<str:pk_test>',
        'deleteProduct':'api/deleteProduct/<str:pk_test>',
    }
    return Response(api_urls)

@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    #return render(request,'main/products.html',{ 'products':products})
    return Response(serializer.data)
    

@api_view(['GET'])
def getProductById(request,pk_test):
    product = Product.objects.get(id=pk_test)
    #return render(request,'main/productById.html',{ 'product':product})
    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH','PUT'])
def updateProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product,  data = request.data, partial =True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProduct(request,pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        return Response("Product deleted successfully!")
    except Product.DoesNotExist:
        raise NotFound(detail="Error 404, ID not found", code=404)


'''
class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main/home.html'

    def get(self, request):
        queryset = {
        'products':'api/products',
        'productById':'api/products/<str:pk_test>',
        'createProduct':'api/createProduct',
        'updateProduct':'api/updateProduct/<str:pk_test>',
        'deleteProduct':'api/deleteProduct/<str:pk_test>',
        }
        return Response({'api_urls':queryset})


class ProductList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main/products.html'

    def get(self, request):
        queryset = Product.objects.all()
        return Response({'products': queryset})
    
class ProductById(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main/productById.html'

    def get(self, request,pk):
        queryset = Product.objects.get(id=pk)
        return Response({'product': queryset})

class CreateProduct(APIView):
    def post(self,request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

'''