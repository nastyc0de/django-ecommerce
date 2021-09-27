from .models import Category
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name', 'slug')
# Register your models here.
admin.site.register(Category, CategoryAdmin)