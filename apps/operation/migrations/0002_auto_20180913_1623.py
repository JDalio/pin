# Generated by Django 2.0.7 on 2018-09-13 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='goodsid',
            field=models.IntegerField(verbose_name='商品id'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='number',
            field=models.IntegerField(verbose_name='商品份数'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='state',
            field=models.IntegerField(verbose_name='商品状态'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='userid',
            field=models.IntegerField(verbose_name='用户id'),
        ),
    ]