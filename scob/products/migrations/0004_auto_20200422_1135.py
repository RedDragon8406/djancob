# Generated by Django 3.0.5 on 2020-04-22 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200415_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.CharField(default='اسکوب', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='topic',
            field=models.CharField(default='', max_length=50),
        ),
    ]