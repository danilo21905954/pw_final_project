# Generated by Django 3.2.5 on 2021-07-03 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libercom', '0013_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizz',
            name='p1',
            field=models.IntegerField(blank=True, verbose_name='p1'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p10',
            field=models.IntegerField(blank=True, verbose_name='p10'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p2',
            field=models.IntegerField(blank=True, verbose_name='p2'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p3',
            field=models.IntegerField(blank=True, verbose_name='p3'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p4',
            field=models.IntegerField(blank=True, verbose_name='p4'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p5',
            field=models.IntegerField(blank=True, verbose_name='p5'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p6',
            field=models.IntegerField(blank=True, verbose_name='p6'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p7',
            field=models.IntegerField(blank=True, verbose_name='p7'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p8',
            field=models.IntegerField(blank=True, verbose_name='p8'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p9',
            field=models.IntegerField(blank=True, verbose_name='p9'),
        ),
        migrations.AlterField(
            model_name='testemunho',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Name'),
        ),
    ]
