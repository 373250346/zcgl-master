from django import forms

from .models import Server, ServerType


# 定义资产表单验证
class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = ['zctype', 'An','Sn','ServerName','SysName','Use','Location','Cabinet','BrandModels',
                  'PurchaseDate','Head','Ipaddress',  'WDate', 'Undernet', 'Comment']


# 定义资产类型表单验证
class ServerTypeForm(forms.ModelForm):
    class Meta:
        model = ServerType
        fields = ['zctype']

