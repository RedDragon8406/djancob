# Generated by Django 3.0.5 on 2020-04-14 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]