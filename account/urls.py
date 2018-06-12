#Author:heming


from django.urls import path,re_path

from . import views

from django.conf import settings
app_name = 'account'
urlpatterns = [
    re_path('^login/$',views.user_login,name='user_login'),
]