
from django.urls import path
from .views import *

urlpatterns = [
    path('',home_page,name='home_page'),
    path('<int:iid>',book_details,name='book_details'),
    path('all_book_details/<int:g_id>',all_book_details,name='all_book_details'),
    path('search',search,name='search'),
]
