from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="coupon code")
    valid_from = models.DateTimeField(verbose_name="start date")
    valid_to = models.DateTimeField(verbose_name="end date")
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Percentage discount"
    )
    active = models.BooleanField(default=True, verbose_name="active")

    class Meta:
        verbose_name = "coupon"
        verbose_name_plural = "coupons"
        ordering = ['-valid_from']

    def __str__(self):
        return self.code
