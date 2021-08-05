from django.contrib import admin
from .models import Product, Category

#teanaadmin 1234qwer

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'parent']
    list_display = ['name', 'parent']


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'prod_slug': ('prod_name',)}
    # fields = ['prod_name', 'prod_description']
    list_display = ['prod_name', 'prod_description', 'prod_category', 'prod_image']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
