from django.db import models
from django.core.exceptions import ValidationError
from apps.category.models import Category, Brand
from mptt.models import TreeForeignKey, MPTTModel
from ecommerce.utils.querysets import ActiveQuerySet
from .fields import OrderField

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True) 
    category = TreeForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    
    objects = ActiveQuerySet.as_manager()
    
    class Meta:
        db_table = "product"
    
    def __str__(self):
        return self.name

class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=6)
    sku = models.CharField(max_length=100)
    stock_qty = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_line")
    is_active = models.BooleanField(default=False)
    order = OrderField(unique_for_field="product", blank=True)
    
    objects = ActiveQuerySet.as_manager()
    
    def clean(self):
        """
        Validate that the order value is unique for the given product.
        """
        super().clean()

        qs = ProductLine.objects.filter(product=self.product)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("Duplicate order value for this product.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ProductLine, self).save(*args, **kwargs)

    
    def __str__(self):
        return str(self.sku)
    

class ProductImage(models.Model):
    alternative_name = models.CharField(max_length=100)
    url = models.ImageField(upload_to=None, default="test.jpg")
    productline = models.ForeignKey(ProductLine, on_delete=models.CASCADE, related_name="product_image")
    order = OrderField(unique_for_field="productline", blank=True)
    
    def clean(self):
        """
        Validate that the order value is unique for the given product.
        """
        super().clean()

        qs = ProductImage.objects.filter(productline=self.productline)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("Duplicate order value for this product.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ProductImage, self).save(*args, **kwargs)
        
    def __str__(self):
        return str(self.url)