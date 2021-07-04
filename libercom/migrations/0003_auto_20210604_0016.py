# Generated by Django 3.2.3 on 2021-06-03 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libercom', '0002_auto_20210603_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testemunho',
            name='apelido',
            field=models.CharField(max_length=30, verbose_name='Apelido'),
        ),
        migrations.AlterField(
            model_name='testemunho',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='testemunho',
            name='testemunho',
            field=models.TextField(max_length=350, verbose_name='Testemunho'),
        ),
        migrations.AlterField(
            model_name='testemunho',
            name='voto',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
        migrations.DeleteModel(
            name='Testimony',
        ),
    ]
