from django.contrib import admin
from .models import Product, ProductLine, ProductImage
from django.urls import reverse
from django.utils.safestring import mark_safe

    
class EditLinkInline:
    def edit(self, instance):
        if instance.pk:  # Ensure the object has been saved and has a primary key
            url = reverse(
                f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
                args=[instance.pk]
            )
            return mark_safe(f'<a href="{url}">Edit</a>')
        return "Not Available"  # Show a placeholder if no PK exists
        
        
class ProductLineInline(EditLinkInline, admin.TabularInline):
    model = ProductLine
    readonly_fields = ("edit",)
    
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]
    

class ProductImageInline(admin.TabularInline):
    model = ProductImage

 
class ProductLineAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductLine, ProductLineAdmin)