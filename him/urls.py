#Author:heming


from django.urls import path,re_path

from . import views
app_name = 'him'
urlpatterns=[
    re_path('^$', views.blog_title,name='blog_title'),
    re_path('(?P<article_id>\d)/$',views.blog_article,name='blog_detail')
]


