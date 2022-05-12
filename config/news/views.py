from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages
from news.forms import NewsForm,UserRegisterForm,UserLoginForm
from news.models import News,Category
from django.contrib.auth import login,logout


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name= 'news'

    def get_queryset(self):
        return News.objects.filter(is_published=True)


#def index(request):
#    news=News.objects.all()
#    context = {
#        'news':news,
#        'title':'List News',
#        'categories':Category.objects.all(),
#    }
#   return render(request,template_name='news/index.html',context=context)

class NewsByCategory(ListView):
    model = News
    template_name='news/index.html'
    context_object_name = 'news'
    extra_context = {'title': 'qanaqadir title'}
    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'] , is_published=True)


#def get_category(request,category_id):
#    print(category_id)
#    #news=News.objects.filter(category_id=category_id),
#    #categories=Category.objects.all(),
#    #category=Category.objects.get(pk=category_id)
#    context ={
#        'news':News.objects.filter(category_id=category_id),
#        'categories':Category.objects.all(),
#        'category':Category.objects.get(pk=category_id)
#    }
#    return render(request,'news/category.html',context)

class ViewNews(DetailView):
    model = News
    template_name = 'news/views_news.html'
    context_object_name= 'news_item'
    #pk_url_kwarg = 'news_id'

#def views_news(request,news_id):
#    news_item=News.objects.get(pk=news_id)
#    categories = Category.objects.all()
#    return render(request,'news/views_news.html',{ 'news_item': news_item,'categories':categories})


# class CreateNews(CreateView):
#     form_class=NewsForm
#     template_name = 'news/add_news.html'
#     success_url = reverse_lazy('home')


def add_news(request):
   if request.method == 'POST':
       form=NewsForm(request.POST)
       print(form.is_valid())
       if  form.is_valid():
           #print(form.cleaned_data)
           #new=News.objects.create(**form.cleaned_data)
           new =form.save()
           return redirect(new)
   else:
       form = NewsForm()
       categories = Category.objects.all()
       cat_count =  Category.news_set.all.count()
       return render(request,'news/add_news.html',{ 'form':form, 'categories':categories,'cat_count':cat_count})

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'register correct!')
            return redirect('login')
        else:
            messages.error(request,'Xatolik')
    else:
        form = UserRegisterForm()
    return render(request,'news/register.html',{ 'form':form })

def user_login(request):
    if request.method == 'POST':
        form= UserLoginForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form=UserLoginForm()
    return render(request,'news/login.html',{'form':form})
def user_logout(request):
    logout(request)
    return redirect('login')