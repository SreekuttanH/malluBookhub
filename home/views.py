from django.core import paginator
from django.db import connection
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.db.models import Q
from django.core.paginator import EmptyPage, Paginator

# Create your views here.

def home_page(request):
    novels_id=1
    poems_id=2
    storys_id=3
    novels=Book.objects.filter(book_category_id=1)[:4]
   

    poems=Book.objects.filter(book_category_id=2)[:4]
    storys=Book.objects.filter(book_category_id=3)[:4]
    return render(request,'index.html',{'book':novels,'poem_book':poems,'story_book':storys,'novels_id':novels_id,'poems_id':poems_id,'storys_id':storys_id})





def book_details(request,iid):
    pk=iid
    data=Book.objects.filter(id=pk)
    return render(request,'book-details.html',{'data':data})



def all_book_details(request,g_id):
    data=Book.objects.filter(book_category_id=g_id)
    paginator=Paginator(data,20)
    
    
    try:
        page=int(request.GET.get('page','1'))
        
    except:
        page=1
    try:
        pro=paginator.page(page)
    except EmptyPage:
        pro=paginator.page(paginator.num_pages)

    return render(request,'all-book-details.html',{'data':pro})
   



def search(request):
    query=None
    bk=None
    if 'search' in request.GET:
        query=request.GET.get('search')
        l_query=query.lower()
        u_query=query.upper()
        t_query=query.title()
        print(l_query)
        bk=Book.objects.all().filter(Q(name__contains=query)|Q(keyword__contains=query)|Q(desc__contains=query)|Q(name__contains=u_query)|Q(name__contains=l_query)|Q(name__contains=t_query))
    else:
        pass

    return render(request,'search.html',{'bk':bk,'q':query})



