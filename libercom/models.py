from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Plano(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=20)
    index = models.IntegerField()
    upload = models.CharField(max_length=20, null=True)
    download = models.CharField(max_length=20, null=True)
    roteador = models.CharField(max_length=50, null=True, blank=True)
    price = models.CharField(verbose_name="Preço", max_length=15, null=True, blank=True)
    icon = models.CharField(verbose_name="Icone", max_length=50, null=True, blank=True)
    destaque = models.BooleanField(verbose_name="Destaque", default=False)
    image_name = models.CharField(verbose_name="Nome do arquivo", max_length=40, blank=True)

    def __str__(self):
        return f"{self.name} MEEGAS= R${self.price},00"


class Contato(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=200)
    birth = models.DateField(verbose_name="Data de Nascimento", null=True, blank=True)
    phone = models.CharField(verbose_name="Telemóvel", max_length=21)
    email = models.EmailField(verbose_name="E-mail", max_length=254)
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE, verbose_name="Plano", related_name="planos")

    def __str__(self):
        return self.name[:200]


class Testemunho(models.Model):
    ESTRELAS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    name = models.CharField(verbose_name="Name", max_length=30)
    apelido = models.CharField(verbose_name="Apelido", max_length=30)
    testemunho = models.TextField(verbose_name="Testemunho", max_length=350)
    enable = models.BooleanField(verbose_name="Visivel", default=True)
    voto = models.IntegerField(verbose_name="Voto", choices=ESTRELAS)

    def __str__(self):
        return f'{self.name} {self.apelido}'


class Quizz(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=200, blank=True)
    p1 = models.IntegerField(verbose_name="p1", blank=True)
    p2 = models.IntegerField(verbose_name="p2", blank=True)
    p3 = models.IntegerField(verbose_name="p3", blank=True)
    p4 = models.IntegerField(verbose_name="p4", blank=True)
    p5 = models.IntegerField(verbose_name="p5", blank=True)
    p6 = models.IntegerField(verbose_name="p6", blank=True)
    p7 = models.IntegerField(verbose_name="p7", blank=True)
    p8 = models.IntegerField(verbose_name="p8", blank=True)
    p9 = models.IntegerField(verbose_name="p9", blank=True)
    p10 = models.IntegerField(verbose_name="p10", blank=True)
    nota = models.IntegerField(verbose_name="Nota", blank=True)

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=200)
    email = models.EmailField(verbose_name="E-mail", max_length=254)

    def __str__(self):
        return self.name
# class Testimony(models.Model):
#     VOTO_CHOICES = (
#         (1, "1"),
#         (2, "2"),
#         (3, "3"),
#         (4, "4"),
#         (5, "5")
#     )
#
#     anonimo = models.BooleanField()
#     testimony = models.TextField(max_length=255)
#     voto = models.IntegerField(choices=VOTO_CHOICES)
#
#
# class Profile(models.Model):
#     first_name = models.CharField(verbose_name="Primeiro Nome", max_length=40)
#     last_name = models.CharField(verbose_name="Último Nome", max_length=40)
#     user = models.CharField(verbose_name="Nome do usuário", max_length=40)
#     password = models.CharField(verbose_name="Senha", max_length=25)
#     phone = models.CharField(verbose_name="Telemóvel", max_length=21)
#     email = models.EmailField(verbose_name="E-mail", max_length=254)
#     birth_date = models.DateField(verbose_name="Data de Nascimento", null=True, blank=True)
#     is_admin = models.BooleanField()
#
#     class Meta:
#         abstract = True
#
#
# class Subscriber(Profile):
#     plano = models.ForeignKey(Plano, on_delete=models.CASCADE, verbose_name="Plano", related_name="plano")
#     testimony = models.ForeignKey(Testimony, on_delete=models.CASCADE, blank=True, null=True,)
#     quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE, blank=True, null=True,)
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
