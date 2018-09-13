from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class Users(AbstractBaseUser):
    avatar_url = models.URLField(verbose_name="头像路径")
    openid = models.CharField(max_length=64, unique=True, verbose_name="用户id")
    nick_name = models.CharField(max_length=30, verbose_name="昵称")
    phone = models.CharField(max_length=11, unique=True, verbose_name="手机号")
    gender = models.BooleanField(default=True, verbose_name="为女生？")
    province=models.CharField(max_length=20,verbose_name='省份')
    city=models.CharField(max_length=20,verbose_name='城市')
    address = models.CharField(
        choices=[('学1', '学1'), ('学2', '学2'), ('学3', '学3'), ('学4', '学4'), ('学5', '学5'), ('学6', '学6'), ('学8', '学8'),
                 ('学9', '学9'), ('学11', '学11'), ('学13', '学13'), ('学29', '学29'), ('留西', '留西'), ('留东', '留东'),
                 ('其他', '其他')], default='学1', max_length=4)
    pick_code = models.CharField(max_length=6, verbose_name='取货码')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class PhoneVerifyCode(models.Model):
    code = models.CharField(max_length=6, verbose_name='手机验证码')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '手机验证码'
        verbose_name_plural = verbose_name
