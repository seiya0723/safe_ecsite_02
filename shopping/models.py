from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Product(models.Model):

    name        = models.CharField(verbose_name="商品名",max_length=200)
    price       = models.IntegerField(verbose_name="価格(円)",validators=[MinValueValidator(0)])

