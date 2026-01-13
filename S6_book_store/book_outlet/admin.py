from django.contrib import admin
from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # See the documentation for more options
    # On list
    list_display = ('title', 'author', 'rating', 'is_bestselling')
    list_filter = ('rating', 'author')

    # On form page
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Book, BookAdmin)
# admin.site.register(Book)
