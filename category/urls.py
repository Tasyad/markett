from django.urls import path
from .views import CategoryListApiView, CategoryCreateApiView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('list/', CategoryListApiView.as_view(), name='list'),
    path('create/', CategoryCreateApiView.as_view(), name='create'),

    ]