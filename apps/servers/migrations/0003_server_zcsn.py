# Generated by Django 2.2.3 on 2020-06-03 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0002_auto_20190806_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='zcsn',
            field=models.CharField(blank=True, max_length=15, verbose_name='资产编号'),
        ),
    ]
