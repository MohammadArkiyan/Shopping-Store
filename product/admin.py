from django.contrib import admin
from .models import Category, Product, Coupon, Color, Size, Image, Comment

admin.site.register(Category)
admin.site.register(Coupon)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Comment)

class ProductImageInline(admin.TabularInline):
    model = Image
    extra = 3
    fields = ('image',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_available')
    prepopulated_fields = {'slug': ('title',)}

    inlines = [ProductImageInline]