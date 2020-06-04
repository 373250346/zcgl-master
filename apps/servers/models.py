from datetime import datetime

from django.db import models

from users.models import UserProfile


# 定义资产model
class Server(models.Model):
    zctype = models.ForeignKey('servers.ServerType', on_delete=models.CASCADE)
    An = models.CharField(max_length=15, verbose_name='资产编号', blank=True)
    Sn = models.CharField(max_length=50, verbose_name='硬件SN号', blank=True)
    ServerName = models.CharField(max_length=50, verbose_name='服务器名称', blank=True)
    SysName = models.CharField(max_length=50, verbose_name='系统全称', blank=True)
    Use = models.CharField(max_length=50, verbose_name='用途', blank=True)
    Location = models.CharField(max_length=50, verbose_name='存放位置', blank=True)
    Cabinet = models.PositiveIntegerField(verbose_name='机柜号', blank=True)
    BrandModels = models.CharField(max_length=50, verbose_name='品牌型号', blank=True)
    PurchaseDate = models.DateTimeField(default=datetime.now, verbose_name='购入日期')
    Head = models.CharField(max_length=50, verbose_name='负责人', blank=True)
    Ipaddress = models.CharField(max_length=100, verbose_name='IP地址', blank=True)
    WDate = models.DateTimeField(default=datetime.now, verbose_name='维保日期')
    Undernet = models.CharField(max_length=10, verbose_name='资产状态')
    Comment = models.CharField(max_length=300, verbose_name='备注', blank=True)
    Modify_time = models.DateTimeField(default=datetime.now, verbose_name='修改时间')
    owner = models.ForeignKey('users.UserProfile', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = '资产表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Undernet


# 定义资产类型model
class ServerType(models.Model):
    zctype = models.CharField(max_length=20, verbose_name='资产类型')

    class Meta:
        verbose_name = '资产类型表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zctype


# 定义资产历史model
class ServerHis(models.Model):
    serverid = models.IntegerField(verbose_name='资产ID')
    zctype = models.CharField(max_length=20, verbose_name='资产类型')
    An = models.CharField(max_length=15, verbose_name='资产编号', blank=True)
    Sn = models.CharField(max_length=50, verbose_name='硬件SN号', blank=True)
    ServerName = models.CharField(max_length=50, verbose_name='服务器名称', blank=True)
    SysName = models.CharField(max_length=50, verbose_name='系统全称', blank=True)
    Use = models.CharField(max_length=50, verbose_name='用途', blank=True)
    Location = models.CharField(max_length=50, verbose_name='存放位置', blank=True)
    Cabinet = models.PositiveIntegerField(verbose_name='机柜号', blank=True)
    BrandModels = models.CharField(max_length=50, verbose_name='品牌型号', blank=True)
    PurchaseDate = models.DateTimeField(default=datetime.now, verbose_name='购入日期')
    Head = models.CharField(max_length=50, verbose_name='负责人', blank=True)
    Ipaddress = models.CharField(max_length=100, verbose_name='IP地址', blank=True)
    WDate = models.DateTimeField(default=datetime.now, verbose_name='维保日期')
    Undernet = models.CharField(max_length=10, verbose_name='资产状态')
    Comment = models.CharField(max_length=300, verbose_name='备注', blank=True)
    Modify_time = models.DateTimeField(default=datetime.now, verbose_name='修改时间')

    class Meta:
        verbose_name = '资产历史表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zctype
