# Generated by Django 3.2.3 on 2021-06-05 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libercom', '0006_auto_20210605_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano',
            name='download',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='plano',
            name='icon',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='plano',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='plano',
            name='price',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='plano',
            name='upload',
            field=models.CharField(max_length=20, null=True),
        ),
    ]