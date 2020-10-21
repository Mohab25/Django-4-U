from django.urls import path,re_path
from .views import *

urlpatterns = [
    re_path(r'Latest/$',Latest.as_view(),name='latest-products'), 
    re_path(r'Latest/(?P<pk>\d+)/$',LatestProduct.as_view()), 
] 

