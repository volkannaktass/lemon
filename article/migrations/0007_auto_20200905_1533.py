# Generated by Django 3.1.1 on 2020-09-05 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20200614_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articledeleterequest',
            name='request_author',
            field=models.CharField(max_length=50, verbose_name='Username'),
        ),
    ]