from django.urls import path
from product import views
urlpatterns = [
    # path('<int:pk>/',views.view_specific_product,name ='product'),
    # path('<int:pk>/',views.ViewSpecificProduct.as_view(),name ='product'),
    # path('<int:pk>/',views.ProductDetails.as_view(),name ='product'),
    # path('',views.view_products,name='product-list')
    # path('',views.ViewProducts.as_view(),name='product-list')
    # path('',views.ListProducts.as_view(),name='product-list')
]
