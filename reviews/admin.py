from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Book, Review

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    search_fields = ('title', 'author')
    list_filter = ('author',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'rating', 'created_at')
    search_fields = ('book__title', 'user__username')
    list_filter = ('rating', 'created_at')
