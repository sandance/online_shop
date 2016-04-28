from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'slug']
    # prepopulated_fields attribute to sepcify fields where value
    # is automatically set
    prepopulated_fields = {'slug' : ('name',) }

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    """
    list_editable attribute in the ProductAdmin class to set the fields
    list_display attribute since only the fields displayed can be edited
    """
    list_display = ['name','slug','price', 'stock',
                    'available', 'created', 'updated'
                    ]

    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)



# Register your models here.
