
import django


from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category, Contact, PostModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def home(request):
    posts = PostModel.objects.all()[:11]
    
    cats = Category.objects.all()
    
    # all_post = Paginator(PostModel.objects.filter)[:3]
    # page = request.GET.get('page')
    
    # try:
    #     postpage = all_post.page(page)
    # except PageNotAnInteger:
    #     postpage = all_post.page(1)
    # except EmptyPage:
    #     postpage = all_post.page(all_post.num_page)
    
    
    data = {
        'posts':posts,
        'cats':cats,
        # 'postpage': postpage
    }
    return render(request, 'home.html', data)

# def base(request):
#     cats = Category.objects.all()
#     print(cats)
    
#     return render(request, 'base.html', {'cats':cats})

def detail(request, url):
    posts = PostModel.objects.all()[:4]
    page = PostModel.objects.get(url = url)
    cats = Category.objects.all() 
    
    
    return render(request, 'detail.html', {'page':page, 'cats':cats, 'posts':posts})

def category(request, url):
    cat = Category.objects.get(url = url)
    posts = PostModel.objects.filter( cat = cat )
    cats = Category.objects.all()
    
    return render(request, 'category.html' , {'cat':cat, 'posts':posts, 'cats':cats })
    

def contact(request):
    # messages.success(request, 'Your message send successfully')
    # messages.error(request, 'Fill your properly')
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
       
        if name == '' or email == '' or message == '':
           messages.error(request, 'Fill your Correctly')
        else:
            contact = Contact(name=name, email=email, message=message)
            contact.save()
            messages.success(request, 'Your message has been send successfully')
            print(name, email, message )
        
       
    return render(request, 'contact.html' )

def search(request):
    query = request.GET['query']
    if len(query) > 80:
        search = PostModel.objects.none()
    else:
        search = PostModel.objects.filter(title__icontains = query)
        
    return render( request, 'search.html', {'search' : search, 'query' : query })

def about(request):
    return render(request, 'about.html')
    

