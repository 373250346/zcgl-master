# Generated by Django 2.2.3 on 2020-06-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0005_auto_20200603_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='zcsn',
        ),
        migrations.RemoveField(
            model_name='serverhis',
            name='zcsn',
        ),
        migrations.AlterField(
            model_name='server',
            name='An',
            field=models.CharField(blank=True, max_length=15, verbose_name='资产编号'),
        ),
        migrations.AlterField(
            model_name='serverhis',
            name='An',
            field=models.CharField(blank=True, max_length=15, verbose_name='资产编号'),
        ),
    ]
