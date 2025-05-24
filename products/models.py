from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Product Name")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Category")
    
    food_day = models.CharField(max_length=200, blank=True, null=True, verbose_name="food day")
    
    nopeople1 = models.DecimalField(max_digits=8 ,decimal_places=0, blank=True, null=True, verbose_name="nopeople1")
    nopeople2 = models.DecimalField(max_digits=8 ,decimal_places=0, blank=True, null=True, verbose_name="nopeople2")
    nopeople3 = models.DecimalField(max_digits=8 ,decimal_places=0, blank=True, null=True, verbose_name="nopeople3")
    nopeople4 = models.DecimalField(max_digits=8 ,decimal_places=0, blank=True, null=True, verbose_name="nopeople4")
    nopeople5_6 = models.DecimalField(max_digits=8 ,decimal_places=0, blank=True, null=True, verbose_name="nopeople5_6")
    nopeople7_8 = models.DecimalField(max_digits=8 ,decimal_places=0, blank=True, null=True, verbose_name="nopeople7_8")

    
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    ingredients = models.TextField(verbose_name="Ingredients",blank=True, null=True)
    price = models.DecimalField(max_digits=8, blank=True, null=True,decimal_places=0, verbose_name="Price")
    image = models.ImageField(upload_to='product_images/', blank=True, null=True ,default='images/default.png') 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name
