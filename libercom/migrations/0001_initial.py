# Generated by Django 3.2.3 on 2021-06-03 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('index', models.IntegerField()),
                ('upload', models.CharField(max_length=50, null=True)),
                ('download', models.CharField(max_length=50, null=True)),
                ('roteador', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(null=True)),
                ('icon', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.CharField(blank=True, max_length=30, verbose_name='p1')),
                ('p2', models.CharField(blank=True, max_length=30, verbose_name='p2')),
                ('p3', models.CharField(blank=True, max_length=30, verbose_name='p3')),
                ('p4', models.CharField(blank=True, max_length=30, verbose_name='p4')),
                ('p5', models.CharField(blank=True, max_length=30, verbose_name='p5')),
                ('p6', models.CharField(blank=True, max_length=30, verbose_name='p6')),
                ('p7', models.CharField(blank=True, max_length=30, verbose_name='p7')),
                ('p8', models.CharField(blank=True, max_length=30, verbose_name='p8')),
                ('p9', models.CharField(blank=True, max_length=30, verbose_name='p9')),
                ('p10', models.CharField(blank=True, max_length=30, verbose_name='p10')),
                ('nota', models.IntegerField(blank=True, verbose_name='Nota')),
            ],
        ),
        migrations.CreateModel(
            name='Testemunho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('apelido', models.CharField(max_length=30)),
                ('testemunho', models.TextField(max_length=350)),
                ('voto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anonimo', models.BooleanField()),
                ('testimony', models.TextField(max_length=255)),
                ('voto', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='Primeiro Nome')),
                ('last_name', models.CharField(max_length=40, verbose_name='??ltimo Nome')),
                ('user', models.CharField(max_length=40, verbose_name='Nome do usu??rio')),
                ('password', models.CharField(max_length=25, verbose_name='Senha')),
                ('phone', models.CharField(max_length=21, verbose_name='Telem??vel')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('is_admin', models.BooleanField()),
                ('plano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plano', to='libercom.plano', verbose_name='Plano')),
                ('quizz', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='libercom.quizz')),
                ('testimony', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='libercom.testimony')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('birth', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('phone', models.CharField(max_length=21, verbose_name='Telem??vel')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('plano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planos', to='libercom.plano', verbose_name='Plano')),
            ],
        ),
    ]
