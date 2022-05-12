from django.contrib import admin
from news.models import News,Category

class NewsAdmin(admin.ModelAdmin):
    list_display= ('id','title','category','created_at','updated_at','is_published')
    search_fields = ('title','content')
    list_display_links = ('id','title')
    list_filter = ('is_published','category')
    list_editable = ('is_published',)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','title')
    search_fields=('title',)
    list_display_links = ('id','title')


admin.site.register(News,NewsAdmin)
admin.site.register(Category,CategoryAdmin)