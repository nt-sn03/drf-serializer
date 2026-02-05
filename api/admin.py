from django.contrib import admin
from django.utils.html import format_html

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('id', 'name')
    empty_value_display = '--empty--'
    
    @admin.display(description='Image')
    def image(self, obj):
        return format_html(
            '<img src="http://localhost:8000/{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;">',
            obj.image.url
        )
