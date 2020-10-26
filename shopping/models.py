from django.db import models
from django.core.validators import MinLengthValidator,MinValueValidator

# Create your models here.
class Product(models.Model):
    class Meta:
        db_table    = "product"

    #商品ID、商品名、商品カテゴリ、価格(円)、
    id          = models.CharField(verbose_name="商品ID(10桁)",primary_key=True,max_length=10,validators=[MinLengthValidator(10)])
    name        = models.CharField(verbose_name="商品名",max_length=200)
    category    = models.CharField(verbose_name="カテゴリ",max_length=20)
    price       = models.IntegerField(verbose_name="価格(円)",validators=[MinValueValidator(0)])

    def __str__(self):
        return self.id



