from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product,Category,Review,ProductImage
from product.serializers import ProductSerializer,CategorySerializer,ReviewSerializer,ProductImageSerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
from product.paginations import DefaultPagination
from rest_framework.permissions import IsAdminUser,AllowAny
from api.permissions import IsAdminOrReadOnly
from rest_framework.permissions import DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from product.permissions import IsReviewAuthorOrReadOnly
from drf_yasg.utils import swagger_auto_schema
# Create your views here.
# @api_view(['GET','POST'])
# def view_products(request):
#     if request.method == 'GET':
#         products = Product.objects.select_related('category').all()
#         serializer = ProductSerializer(products,many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = ProductSerializer(data=request.data) #Deserializer
#         serializer.is_valid(raise_exception=True)
#         print(serializer.valpkated_data)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
# class ViewProducts(APIView):
#     def get(self,request):
#         products = Product.objects.select_related('category').all()
#         serializer = ProductSerializer(products,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = ProductSerializer(data=request.data) #Deserializer
#         serializer.is_valid(raise_exception=True)
#         print(serializer.valpkated_data)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
       
# class ListProducts(ListCreateAPIView):
#     def get_queryset(self):
#         return  Product.objects.select_related('category').all()
#     def get_serializer_class(self):
#         return ProductSerializer
    
# @api_view(['GET','PUT','DELETE'])
# def view_specific_product(request,pk):
#     if request.method =='GET':
#         product = get_object_or_404(Product,pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     if request.method =='PUT':
#         product = get_object_or_404(Product,pk=pk)
#         serializer = ProductSerializer(product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     if request.method == 'DELETE':
#         product = get_object_or_404(Product,pk=pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ViewSpecificProduct(APIView):
#     def get(self,request,pk):
#         product = get_object_or_404(Product,pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     def put(self,request,pk):
#         product = get_object_or_404(Product,pk=pk)
#         serializer = ProductSerializer(product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self,request,pk):
#         product = get_object_or_404(Product,pk=pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# class ProductDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class ProductViewSet(ModelViewSet):
    """
    API endpint for managing products in the e-commerce store
    - Allow authenticated admin to create,update, and delete products
    - Allow users to browse and filter product
    - Support searching by name,description,and category
    - Support ordering by price and updated_at
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends =[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = ProductFilter
    # pagination_class = PageNumberPagination
    pagination_class = DefaultPagination
    # filterset_fields =['category_id','price']
    search_fields =['name','description']
    ordering_fields =['price','updated_at']
    permission_classes = [IsAdminOrReadOnly]
    @swagger_auto_schema(
            operation_summary ="Retrive a list of products"
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the product"""
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
            operation_summary ="Create a product by admin",
            responses={
                201: ProductSerializer,
                400: 'Bad Request'
            }
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated admin can create product"""
        return super().create(request, *args, **kwargs)
    # permission_classes =[DjangoModelPermissions]
    # permission_classes =[DjangoModelPermissionsOrAnonReadOnly]
    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [AllowAny()]
    #     return [IsAdminUser()]
    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     category_id = self.request.query_params.get('category_id')
    #     if category_id is not None:
    #         queryset = Product.objects.filter(category_id=category_id)
    #     return queryset
class ProductImageViewSet(ModelViewSet):
   serializer_class = ProductImageSerializer
   permission_classes =[IsAdminOrReadOnly]
   def get_queryset(self):
       return ProductImage.objects.filter(product_id=self.kwargs.get('product_pk'))
   def perform_create(self, serializer):
       serializer.save(product_id=self.kwargs.get('product_pk'))
    
# @api_view()
# def view_categories(request):
#     categories = Category.objects.annotate(product_count = Count('products')).all()
#     serializer = CategorySerializer(categories,many=True)
#     return Response(serializer.data)

# class ViewCategories(APIView):
#     def get(self,request):
#         categories = Category.objects.annotate(product_count = Count('products')).all()
#         serializer = CategorySerializer(categories,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer =CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
    
# # class CategoryList(ListCreateAPIView):
#     queryset =  Category.objects.annotate(product_count = Count('products')).all()
#     serializer_class = CategorySerializer
#     # jodi kono logical kono kisu na lage tahole override korar dorkar hobe na uporer line gulu likhle hobe
    # def get_queryset(self):
    #     return Category.objects.annotate(product_count = Count('products')).all()
    # def get_serializer_class(self):
    #     return CategorySerializer
# @api_view()
# def view_specific_categories(request,pk):
#     category = get_object_or_404(Category,pk=pk)
#     serializer = CategorySerializer(category)
#     return Response(serializer.data)

# class ViewSpecificCategory(APIView):
#     def get(self,request,pk):
#         category = get_object_or_404(Category.objects.annotate(product_count = Count('products')).all(),pk=pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         category = get_object_or_404(Category,pk=pk)
#         serializer = CategorySerializer(category,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self,request,pk):
#         category = get_object_or_404(Category,pk=pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CategoryDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count = Count('products')).all()
    serializer_class = CategorySerializer
    permission_classes =[IsAdminOrReadOnly]

class ReviewViewSet(ModelViewSet):
    
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs.get('product_pk'))
    def get_serializer_context(self):
        return {'product_id':self.kwargs.get('product_pk')}