from django.urls import path,include
from rest_framework import routers
from rest_framework_nested import routers
from product.views import ProductViewSet,CategoryViewSet,ReviewViewSet,ProductImageViewSet
from order.views import CartViewSet,CartItemViewSet,OrderViewSet,initiate_payment,payment_success,payment_cancel,payment_fail

router = routers.DefaultRouter()
router.register('products',ProductViewSet,basename='products')
router.register('categories',CategoryViewSet)
router.register('carts',CartViewSet,basename='carts')
router.register('orders',OrderViewSet,basename='orders')

product_router = routers.NestedDefaultRouter(router,'products',lookup='product')
product_router.register('reviews',ReviewViewSet,basename='product-review')
product_router.register('images',ProductImageViewSet,basename='product-image')

cart_router = routers.NestedDefaultRouter(router,'carts',lookup='cart')
cart_router.register('items',CartItemViewSet,basename='cart-item')
# urlpatterns = router.urls
# jodi amar aro path thake tahole nicher motw kore dibo ar nahole uporer line ta likhe dilei hobe
urlpatterns =[
    path('',include(router.urls)),
    path('',include(product_router.urls)),
    path('',include(cart_router.urls)),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    path('payment/initiate/',initiate_payment, name='initiate-payment'),
    path('payment/success/',payment_success, name='payment-success'),
    path('payment/cancel/',payment_cancel, name='payment-cancel'),
    path('payment/fail/',payment_fail, name='payment-fail')
]

# urlpatterns = [
#     path('products/',include('product.product_urls')),
#     path('categories/',include('product.category_urls')),
# ]
