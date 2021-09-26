from django.urls import path
from .views import *

urlpatterns = [
    path('user_login',user_login,name='user_login'),
    path('user_reg',user_reg,name='user_reg'),
    path('user_reg_action',user_reg_action,name='user_reg_action'),
    path('user_login_action',user_login_action,name='user_login_action'),
    path('user_logout',user_logout,name='user_logout'),
]
