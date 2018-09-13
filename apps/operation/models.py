from datetime import datetime

from django.db import models

# Create your models here.
class Operation(models.Model):
    userid=models.IntegerField(verbose_name='用户id')
    goodsid=models.IntegerField(verbose_name='商品id')
    number=models.IntegerField(verbose_name='商品份数')
    state=models.IntegerField(verbose_name='操作状态')
    operation_time=models.DateTimeField(default=datetime.now,verbose_name='操作时间')

    class Meta:
        verbose_name='购买信息'
        verbose_name_plural=verbose_name