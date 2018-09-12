from django.db import models

# Create your models here.
class Users(models.Model):
    openid=models.CharField(max_length=64,verbose_name="用户id")
    nick_name=models.CharField(max_length=20,verbose_name="昵称")
    phone=models.CharField(max_length=11,verbose_name="手机号")
    address=models.CharField(choices=[])
    gender=models.BooleanField()