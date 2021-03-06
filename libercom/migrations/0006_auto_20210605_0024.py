# Generated by Django 3.2.3 on 2021-06-04 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libercom', '0005_testemunho_enable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizz',
            name='p1',
            field=models.IntegerField(blank=True, max_length=30, verbose_name='p1'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p10',
            field=models.IntegerField(blank=True, max_length=30, verbose_name='p10'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p2',
            field=models.IntegerField(blank=True, max_length=30, verbose_name='p2'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p3',
            field=models.IntegerField(blank=True, max_length=30, verbose_name='p3'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p4',
            field=models.IntegerField(blank=True, max_length=30, verbose_name='p4'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p5',
            field=models.IntegerField(blank=True, max_length=30, verbose_name='p5'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p6',
            field=models.IntegerField(blank=True, max_length=30, verbose_name='p6'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p7',
            field=models.IntegerField(blank=True, max_length=30, verbose_name='p7'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p8',
            field=models.IntegerField(blank=True, max_length=30, verbose_name='p8'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='p9',
            field=models.IntegerField(blank=True, max_length=30, verbose_name='p9'),
        ),
        migrations.AlterField(
            model_name='testemunho',
            name='voto',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Voto'),
        ),
    ]
