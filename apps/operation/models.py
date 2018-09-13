from django.db import models

# Create your models here.
class Operation(models.Model):
    userid=models.IntegerField(max_length=6,verbose_name='用户id')
    goodsid=models.IntegerField(max_length=6,verbose_name='商品id')
    number=models.IntegerField(max_length=6,verbose_name='商品份数')
    state=models.IntegerField(max_length=2,verbose_name='商品状态')

    class Meta:
        verbose_name='购买状态'
        verbose_name_plural=verbose_name