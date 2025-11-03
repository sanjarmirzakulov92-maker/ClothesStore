from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name="Name of category")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Article(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name="Name of article")
    content = models.TextField(verbose_name="Description")
    photo = models.ImageField(upload_to="Photos/", null=True, blank=True, verbose_name="Pictures")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated")
    publish = models.BooleanField(default=True, verbose_name="Publish")
    views = models.IntegerField(default=0, verbose_name="View")
    price = models.DecimalField(max_digits=10, decimal_places=3 ,verbose_name="Price")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Category")


    def get_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return None


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

