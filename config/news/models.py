from django.db import models

# Create your models here.
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150,verbose_name='Sarlavha')
    content = models.TextField(blank=True,verbose_name='Sarlavha matni')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='yaratilgan vaqt')
    updated_at = models.DateTimeField(auto_now=True,verbose_name="o'zgartirilgan vaqt")
    image = models.ImageField(upload_to='photo/%Y/%m/%d/',verbose_name='rasm',blank=True)
    is_published = models.BooleanField(default=True,verbose_name='bilmadim')
    category = models.ForeignKey('Category',on_delete=models.PROTECT,null=True)

    def get_absolute_url(self):
        return reverse('views_news', kwargs={ 'pk': self.pk })

    def __str__(self):
        return self.title



    class Meta:
        verbose_name='Yangiliklar'
        verbose_name_plural='YANGILIK'
        ordering=('-created_at',)


        
class Category(models.Model):
    title = models.CharField(max_length=150,db_index=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Category'
        verbose_name_plural='category'

    def get_absolute_url(self):
        return reverse('category',kwargs={ 'category_id':self.pk })