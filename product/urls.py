from django.urls import path
from .views import ProductListApiView, ProductCreateApiView, ProductDetailApiView, ProductUpdateApiView, \
    ProductDestroyApiView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('list/', ProductListApiView.as_view(), name='list'),
    path('create/', ProductCreateApiView.as_view(), name='create'),
    path('detail/<int:id>/', ProductDetailApiView.as_view(), name='detail'),
    path('update/<int:id>/', ProductUpdateApiView.as_view(), name='update'),
    path('delete/<int:id>/', ProductDestroyApiView.as_view(), name='delete'),
]