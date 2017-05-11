from django.contrib import admin
from .models import Product
# Register your models here.
#admin.site.register(Product)
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'Nombre', 'Categoria', 'Descripcion', 'Precio')
    list_filter = ('Categoria',)