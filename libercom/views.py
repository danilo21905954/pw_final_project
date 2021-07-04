from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime

from django.urls import reverse

from .models import *
from .forms import ContatoForm, TestemunhoForm


# Create your views here.
def home_page_view(request):
    context = {
        'year': datetime.date.today().year,
        'testemunho': Testemunho.objects.all(),
        'planos': Plano.objects.all().order_by('index'),
    }
    return render(request, 'libercom/home.html', context)


def add_page_view(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('libercom:success'))

    context = {'form': form, 'year': datetime.date.today().year}
    return render(request, 'libercom/add.html', context)


def success_view(request):
    context = {'year': datetime.date.today().year}
    return render(request, 'libercom/success.html', context)


def quizz_view(request):
    if request.method == "POST":
        name = request.POST['name']
        p1 = int(request.POST['p1'])
        p2 = int(request.POST['p2'])
        p3 = int(request.POST['p3'])
        p4 = int(request.POST['p4'])
        p5 = int(request.POST['p5'])
        p6 = int(request.POST['p6'])
        p7 = int(request.POST['p7'])
        p8 = int(request.POST['p8'])
        p9 = int(request.POST['p9'])
        p10 = int(request.POST['p10'])

        nota = 0

        if p1 == 1:
            nota += 10

        if p2 == 4:
            nota += 10

        if p3 == 1:
            nota += 10

        if p4 == 4:
            nota += 10

        if p5 == 1:
            nota += 10

        if p6 == 2:
            nota += 10

        if p7 == 1:
            nota += 10

        if p8 == 1:
            nota += 10

        if p9 == 1:
            nota += 10

        if p10 == 1:
            nota += 10

        q = Quizz(
            name=name,
            p1=p1, p2=p2, p3=p3, p4=p4, p5=p5,
            p6=p6, p7=p7, p8=p8, p9=p9, p10=p10,
            nota=nota
        )
        q.save()

        context = {'name': name, 'nota': nota, 'year': datetime.date.today().year}
        return render(request, 'libercom/nota.html', context)

    context = {'year': datetime.date.today().year}
    return render(request, 'libercom/quizz.html', context)


def plano_view(request):
    context = {
        'year': datetime.date.today().year,
        'planos': Plano.objects.all().order_by('index'),
    }
    return render(request, 'libercom/pricing.html', context)


def sobre_view(request):
    context = {'year': datetime.date.today().year, 'testemunho': Testemunho.objects.all()}
    return render(request, 'libercom/about.html', context)


def sitemap_view(request):
    context = {'year': datetime.date.today().year}
    return render(request, 'libercom/sitemap.html', context)


def add_testemunho_view(request):
    form = TestemunhoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('libercom:add-testemunho-success'))

    context = {'form': form, 'year': datetime.date.today().year}
    return render(request, 'libercom/testemunho_add.html', context)


def add_testemunho_success_view(request):
    return render(request, 'libercom/success_testemunho.html', {'year': datetime.date.today().year})
