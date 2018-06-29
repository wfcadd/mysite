#Author:heming


from django.urls import path,re_path

from . import views

from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.conf import settings
app_name = 'account'
urlpatterns = [
    #re_path('^login/$',views.user_login,name='user_login'),
    #re_path('^login/$',auth_views.login,name='user_login'),
    re_path('^new-login/$',auth_views.login,{"template_name":"account/login.html"},name='user_login'),
    re_path('^logout/$',auth_views.logout,{"template_name":"account/logged_out.html"},name='user_logout'),
    re_path('^register/$',views.register,name='user_register'),
]