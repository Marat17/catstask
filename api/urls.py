from django.urls import path, re_path
from . import views

urlpatterns = [
    path( '', views.CatList.as_view(), name = 'cat_list' ),
    re_path( r'^cats/(?P<pk>[0-9]+)$', views.CatDetail.as_view(), name = 'cat_detail' ),
]