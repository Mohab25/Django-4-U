from django.urls import path,re_path
from .views import *

urlpatterns = [
    re_path(r'products/$',AllProducts.as_view(),name='all-products'),
    re_path(r'Latest/$',Latest.as_view(),name='latest-products'), 
    re_path(r'Latest/(?P<pk>\d+)/$',LatestProduct.as_view()), 
    re_path(r'Samsung/$',Samsung.as_view(),name='samsung-list'),
    re_path(r'Samsung_Gallery/$',Samsung_Gallery.as_view(),name='samsung-gallery'),
    re_path(r'Samsung/(?P<pk>\d+)/$',Samsung_product.as_view(),name='samsung-product'),
    re_path(r'Apple/$',Apple.as_view(),name='apple-list'),
    re_path(r'Apple_Gallery/$',Apple_Gallery.as_view(),name='apple-gallery'),
    re_path(r'Apple/(?P<pk>\d+)/$',Apple_product.as_view(),name='apple-product'),
    re_path(r'Huawei/$',Huawei.as_view(),name='huawei-list'),
    re_path(r'Huawei_Gallery/$',Huawei_Gallery.as_view(),name='huawei-gallery'),
    re_path(r'Huawei/(?P<pk>\d+)/$',Huawei_product.as_view(),name='huawei-product'),
] 

