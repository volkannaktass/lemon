# Generated by Django 2.2.6 on 2020-03-29 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20200329_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='about',
            field=models.CharField(max_length=200, verbose_name='What is the subject of the Article'),
        ),
    ]
