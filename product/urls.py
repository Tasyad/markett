from django.urls import path
from .views import ProductListApiView, ProductCreateApiView, ProductDetailApiView, ProductUpdateApiView, \
    ProductDestroyApiView, CategoryDetailApiView
from django.urls import path
from .views import CategoryListApiView, CategoryCreateApiView


urlpatterns = [
    path('prod_list/', ProductListApiView.as_view(), name='prod_list'),
    path('create/', ProductCreateApiView.as_view(), name='create'),
    path('detail/<int:id>/', ProductDetailApiView.as_view(), name='detail'),
    path('update/<int:id>/', ProductUpdateApiView.as_view(), name='update'),
    path('delete/<int:id>/', ProductDestroyApiView.as_view(), name='delete'),
    path('cat_list/', CategoryListApiView.as_view(), name='cat_list'),
    path('cat_create/', CategoryCreateApiView.as_view(), name='cat_create'),
    path('filter/<slug:name>/', CategoryDetailApiView.as_view(), name='cat_category'),
]
