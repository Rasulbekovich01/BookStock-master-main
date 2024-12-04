from re import A
from django.contrib import admin
from stock.models import Category, Book, AdditionalInfo, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        'created_at',  
    )
    search_fields = ('name',)  
    list_filter = ('created_at',)


class AdditionalInfoInline(admin.TabularInline):
    model = AdditionalInfo
    extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'title', 
        'author', 
        'price', 
        'quantity', 
        'isbn', 
        'sku', 
        'rating',
    )
    search_fields = ('title', 'author', 'isbn', 'sku')  
    list_filter = ('categories', 'price', 'quantity') 
    filter_horizontal = ('categories',)  
    inlines = [AdditionalInfoInline]


@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'book', 
        'name', 
        'desc',
    )
    search_fields = ('name', 'desc', 'book__title') 
    list_filter = ('book',) 




@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'book', 
        'user', 
        'rating', 
        'text', 
        'created_at',
    )
    search_fields = ('user__username', 'book__title', 'text')  
    list_filter = ('rating', 'created_at')  



