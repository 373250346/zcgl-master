# Generated by Django 2.2.3 on 2020-06-03 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0004_serverhis_zcsn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='Cabinet',
            field=models.PositiveIntegerField(blank=True, verbose_name='机柜号'),
        ),
        migrations.AlterField(
            model_name='server',
            name='Comment',
            field=models.CharField(blank=True, max_length=300, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='server',
            name='Head',
            field=models.CharField(blank=True, max_length=50, verbose_name='负责人'),
        ),
        migrations.AlterField(
            model_name='server',
            name='Ipaddress',
            field=models.CharField(blank=True, max_length=100, verbose_name='IP地址'),
        ),
        migrations.AlterField(
            model_name='server',
            name='Location',
            field=models.CharField(blank=True, max_length=50, verbose_name='存放位置'),
        ),
        migrations.AlterField(
            model_name='server',
            name='PurchaseDate',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='购入日期'),
        ),
        migrations.AlterField(
            model_name='server',
            name='Undernet',
            field=models.CharField(max_length=10, verbose_name='资产状态'),
        ),
        migrations.AlterField(
            model_name='serverhis',
            name='Cabinet',
            field=models.PositiveIntegerField(blank=True, verbose_name='机柜号'),
        ),
        migrations.AlterField(
            model_name='serverhis',
            name='Comment',
            field=models.CharField(blank=True, max_length=300, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='serverhis',
            name='Head',
            field=models.CharField(blank=True, max_length=50, verbose_name='负责人'),
        ),
        migrations.AlterField(
            model_name='serverhis',
            name='Ipaddress',
            field=models.CharField(blank=True, max_length=100, verbose_name='IP地址'),
        ),
        migrations.AlterField(
            model_name='serverhis',
            name='Location',
            field=models.CharField(blank=True, max_length=50, verbose_name='存放位置'),
        ),
        migrations.AlterField(
            model_name='serverhis',
            name='PurchaseDate',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='购入日期'),
        ),
        migrations.AlterField(
            model_name='serverhis',
            name='Undernet',
            field=models.CharField(max_length=10, verbose_name='资产状态'),
        ),
    ]
