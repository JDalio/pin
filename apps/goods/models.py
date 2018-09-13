from datetime import datetime

from django.db import models


# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='商品名')
    grow_place = models.CharField(max_length=20, verbose_name='产地')
    delicious_time = models.CharField(max_length=20, verbose_name='何时好吃')
    price = models.FloatField(verbose_name='售价')
    goods_cost = models.FloatField(verbose_name='商品进价成本')
    packing_cost = models.FloatField(verbose_name='商品包装成本')
    kind = models.IntegerField(verbose_name='商品种类')
    is_new=models.BooleanField(default=False,verbose_name='是否为新品')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='加入时间')

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name
