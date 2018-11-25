from django.urls import re_path, path
from cats import views

urlpatterns = [
    re_path(r'^login/$', views.LoginFormView.as_view(), name='login'),
    re_path(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    path('', views.show_my_cats, name='index'),
        ]