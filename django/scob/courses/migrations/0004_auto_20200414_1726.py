# Generated by Django 3.0.5 on 2020-04-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20200414_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]