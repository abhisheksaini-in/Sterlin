from django.contrib import admin
from .models import PostModel, Category, Contact

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display  = ('title','add_date',)
    search_fields = ('title',)
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'add_date',)
    search_fields = ('name',)
    list_per_page = 15
    
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','add_date',)
    search_fields = ('title',)
    list_per_page = 15
   
    


admin.site.register(PostModel, CategoryAdmin)
admin.site.register(Category, PostModelAdmin)
admin.site.register(Contact, ContactAdmin)
