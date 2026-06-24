from django.contrib import admin

# Register your models here.
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','counted_views','status','published_date','created_date','updated_date') 
    list_filter = ('status','published_date','created_date','updated_date')
   # ordering = ('status','published_date','-created_date','-updated_date')
    search_fields = ('title','content')
admin.site.register(Post,PostAdmin)