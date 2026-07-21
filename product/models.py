from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    """ A category that include some products. """

    title = models.CharField(max_length=200, verbose_name='title')
    image = models.ImageField(upload_to='images/categories', null=True, blank=True, verbose_name='image')
    is_featured = models.BooleanField(default=False, verbose_name='featured', help_text='Is this a featured category?')
    date_added = models.DateField(auto_now_add=True, verbose_name='date added')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Color(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    date_added = models.DateField(auto_now_add=True, verbose_name=' date added')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class Size(models.Model):
    title = models.CharField(max_length=100, verbose_name='name')
    date_added = models.DateField(auto_now_add=True, verbose_name='date added')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'


class Product(models.Model):
    """ A product that add-in site. """

    category = models.ManyToManyField(Category, related_name='categories')
    color = models.ManyToManyField(Color, related_name='colors')
    size = models.ManyToManyField(Size, related_name='sizes', blank=True)
    title = models.CharField(max_length=200, verbose_name='title')
    description = models.TextField(verbose_name='description')
    is_available = models.BooleanField(default=True, verbose_name='is available', help_text='Is this product available?')
    is_featured = models.BooleanField(default=False, verbose_name='is featured', help_text='Is this a featured product?')
    price = models.DecimalField(max_digits=14, decimal_places=2, verbose_name='price')
    discount_percentage = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='discount percent')
    date_added = models.DateField(auto_now_add=True, verbose_name='date added')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='The date of the last update')
    slug = models.SlugField(verbose_name='slug')

    def get_discount_price(self):
        """ Calculate discount of price. """

        discount = self.discount_percentage or 0
        return (self.price * discount) / 100

    def product_price_processor(self):
        """ Calculate price after discount of price. """

        discount_amount = self.get_discount_price()
        return self.price - discount_amount

    def get_main_image(self):
        """ Get main or first image for product cover """

        first_image_obj = self.images.first()

        if first_image_obj and first_image_obj.image:
            return first_image_obj.image.url

        return '/static/default.jpg'

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'pk': self.pk})

    def __str__(self):
        """ return a string representation of the product model. """

        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Image(models.Model):
    # when we want to access from special product to its images we use related_name > images
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', null=True)
    image = models.ImageField(upload_to='images/products', help_text='Please enter an image of your product.',
                              null=True, blank=True)
    date_added = models.DateField(auto_now_add=True, verbose_name='date added')

    def __str__(self):
        return f"image for {self.product.title}"

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'


class Coupon(models.Model):
    title = models.CharField(max_length=200, verbose_name='discount subject')
    code = models.CharField(max_length=200, verbose_name='discount code')
    date_added = models.DateField(auto_now_add=True, verbose_name='date added')
    expiration_date = models.DateTimeField()
    is_available = models.BooleanField(help_text='Is there a discount code available?')

    def is_valid(self):
        """ Check The coupon is available or not with expiration_date. """

        return self.expiration_date > timezone.now() and self.is_available

    def is_available(self):
        """ Change is_available value to False if the coupon time expired. """

        if self.expiration_date < timezone.now():
            self.is_available = False

    def __str__(self):
        return f'{self.title} discount coupon'

    class Meta:
        verbose_name = 'discount'
        verbose_name_plural = 'discounts'


# product/models.py

from django.contrib.auth.models import User
from django.db import models




class Comment(models.Model):

    product = models.ForeignKey('Product', models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, models.CASCADE, related_name='comments', null=True,
                             blank=True)

    body = models.TextField(verbose_name='comment text')
    email = models.EmailField(verbose_name='email', null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name='name', null=True, blank=True)

    is_active = models.BooleanField(default=False, verbose_name='Publication status',
                                    help_text='Has the comment been approved by the administrator?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of registration')

    def __str__(self):
        return f'Comment by {self.name or self.user.username} on {self.product.title}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
