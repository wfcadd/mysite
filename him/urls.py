#Author:heming


from django.urls import path,re_path

from . import views

urlpatterns=[
    re_path('^$', views.blog_title,name='blog_title')
]