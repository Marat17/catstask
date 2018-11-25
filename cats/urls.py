from django.urls import re_path, path
from cats import views

urlpatterns = [
    re_path(r'^login/$', views.LoginFormView.as_view(), name='login'),
    re_path(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    re_path(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    re_path(r'^create/$', views.cat_create, name='cat_create'),
    path('edit/<int:id>/', views.cat_edit, name='cat_edit'),
    path('delete/<int:id>/', views.cat_delete, name='cat_delete'),
        ]