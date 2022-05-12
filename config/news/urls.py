from django.urls import path

from news.views import  *

urlpatterns = [
    #path('',index,name='home'),
    path('',HomeNews.as_view(),name='home'),
    #path('category/<int:category_id>/',get_category, name='category'),
    path('category/<int:category_id>/',NewsByCategory.as_view(), name='category'),
    #path('news/<int:news_id>/',views_news, name='views_news'),
    path('news/<int:pk>/',ViewNews.as_view(), name='views_news'),
    path('news/add_news/',add_news, name='add_news'),
    #path('news/add_news/',CreateNews.as_view(), name='add_news'),
    path('register/',register,name='register'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
]