from django.db import models
from django.urls import reverse


class branch(models.Model):
    name = models.CharField(max_length=30)
    add = models.URLField(unique=True)


    def __str__(self):
        return self.name

class category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    branch = models.ForeignKey(branch, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('taskapp:all',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    des = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'


    def get_url(self):
        return reverse('taskapp:allpro',args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class accoun(models.Model):
    name=models.CharField(max_length=250,blank=True)
    addr=models.TextField(blank=True)
    phone=models.IntegerField(blank=True)
    date_add=models.DateField(auto_now_add=True)

    class Meta:
        db_table='accoun'
        ordering=['date_add']
    def __str__(self):
        return '{}'.format(self.name)