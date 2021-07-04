import datetime

from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib import auth

# Create your views here.
from libercom.forms import *
from libercom.models import *
from users.utils import get_graphs


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('users:home'))
        else:
            return render(request, 'libercom/home.html', {
                'message': 'Credenciais inválidas.',
                'year': datetime.date.today().year,
            })

    return HttpResponseRedirect(reverse('libercom:home'))


def user_view(request):
    if request.user.is_authenticated:
        context = {'year': datetime.date.today().year, 'option': 1}
        return render(request, "users/index.html", context)

    return render(request, 'libercom/home.html', {
        'message': 'Sem permissão para acessar esta página. Realize o login e tente novamente',
        'year': datetime.date.today().year,
    })


def logout_view(request):
    logout(request)
    auth.logout(request)
    return HttpResponseRedirect(reverse('libercom:home'))


def testemunho_view(request):
    if not request.user.is_authenticated:
        return render(request, 'libercom/home.html', {
            'message': 'Sem permissão para acessar esta página. Realize o login e tente novamente',
            'year': datetime.date.today().year,
        })

    context = {'form': Testemunho.objects.all(), 'year': datetime.date.today().year, 'option': 2}
    return render(request, 'users/testemunhos.html', context)


def testemunho_delete_view(request, testemunho_id):
    if not request.user.is_authenticated:
        return render(request, 'libercom/home.html', {
            'message': 'Sem permissão para acessar esta página. Realize o login e tente novamente',
            'year': datetime.date.today().year,
        })

    context = {'testemunho_id': testemunho_id, 'year': datetime.date.today().year, 'option': 2}
    return render(request, "users/testemunho_delete.html", context)


def testemunho_delete_confirmed_view(request, testemunho_id):
    Testemunho.objects.get(id=testemunho_id).delete()
    return HttpResponseRedirect(reverse('users:testemunho'))


def testemunho_edit_view(request, testemunho_id):
    if not request.user.is_authenticated:
        return render(request, 'libercom/home.html', {
            'message': 'Sem permissão para acessar esta página. Realize o login e tente novamente',
            'year': datetime.date.today().year,
        })

    testemunho = Testemunho.objects.get(id=testemunho_id)
    form = TestemunhoAdminForm(request.POST or None, instance=testemunho)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('users:testemunho'))

    context = {'form': form, 'testemunho_id': testemunho_id, 'year': datetime.date.today().year, 'option': 2}
    return render(request, "users/testemunho_edit.html", context)


def exit_view(request):
    if not request.user.is_authenticated:
        return render(request, 'libercom/home.html', {
            'message': 'Sem permissão para acessar esta página. Realize o login e tente novamente',
            'year': datetime.date.today().year,
        })
    return render(request, "users/exit.html", {'year': datetime.date.today().year})


def quizz_view(request):
    if not request.user.is_authenticated:
        return render(request, 'libercom/home.html', {
            'message': 'Sem permissão para acessar esta página. Realize o login e tente novamente',
            'year': datetime.date.today().year,
        })
    context = {'quizz': Quizz.objects.all(), 'year': datetime.date.today().year, 'option': 4}
    return render(request, 'users/quizz.html', context)


def statistics_view(request):
    if not request.user.is_authenticated:
        return render(request, 'libercom/home.html', {
            'message': 'Sem permissão para acessar esta página. Realize o login e tente novamente',
            'year': datetime.date.today().year,
        })

    context = {
        'contatos': len(Contato.objects.all()),
        'planos': len(Plano.objects.all()),
        'testemunho': len(Testemunho.objects.all()),
        'quizz': len(Quizz.objects.all()),
        'year': datetime.date.today().year,
        'option': 5,
    }
    return render(request, "users/statistics.html", context)


def statistics_data(request):
    graficos = get_graphs()

    # Return list of posts
    return JsonResponse(graficos)


def plano_view(request):
    if not request.user.is_authenticated:
        return render(request, 'libercom/home.html', {
            'message': 'Sem permissão para acessar esta página. Realize o login e tente novamente',
            'year': datetime.date.today().year,
        })

    context = {'planos': Plano.objects.all(), 'year': datetime.date.today().year, 'option': 6}
    return render(request, 'users/planos.html', context)


def plano_new_view(request):
    if not request.user.is_authenticated:
        return render(request, 'libercom/home.html', {
            'message': 'Sem permissão para acessar esta página. Realize o login e tente novamente',
            'year': datetime.date.today().year,
        })

    form = PlanoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('users:planos'))

    context = {'form': form, 'year': datetime.date.today().year, 'option': 6}
    return render(request, 'users/plano_new.html', context)


def plano_edit_view(request, plano_id):
    if not request.user.is_authenticated:
        return render(request, 'libercom/home.html', {
            'message': 'Sem permissão para acessar esta página. Realize o login e tente novamente',
            'year': datetime.date.today().year,
        })

    plano = Plano.objects.get(id=plano_id)
    form = PlanoForm(request.POST or None, instance=plano)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('users:planos'))

    context = {'form': form, 'plano_id': plano_id, 'year': datetime.date.today().year, 'option': 6}
    return render(request, "users/plano_edit.html", context)


def plano_delete_view(request, plano_id):
    if not request.user.is_authenticated:
        return render(request, 'libercom/home.html', {
            'message': 'Sem permissão para acessar esta página. Realize o login e tente novamente',
            'year': datetime.date.today().year,
        })

    context = {'year': datetime.date.today().year, 'plano': Plano.objects.get(pk=plano_id), 'option': 6}
    return render(request, 'users/plano-delete.html', context)


def plano_delete_confirmed_view(request, plano_id):
    Plano.objects.get(id=plano_id).delete()
    return HttpResponseRedirect(reverse('users:planos'))


def users_view(request):
    if not request.user.is_authenticated:
        return render(request, 'libercom/home.html', {
            'message': 'Sem permissão para acessar esta página. Realize o login e tente novamente',
            'year': datetime.date.today().year,
        })

    context = {'year': datetime.date.today().year, 'contatos': Contato.objects.all(), 'option': 3}
    return render(request, "users/users.html", context)


def users_delete_view(request, contato_id):
    if not request.user.is_authenticated:
        return render(request, 'libercom/home.html', {
            'message': 'Sem permissão para acessar esta página. Realize o login e tente novamente',
            'year': datetime.date.today().year,
        })
    context = {'year': datetime.date.today().year, 'contato': Contato.objects.get(pk=contato_id), 'option': 3}
    return render(request, 'users/users-delete.html', context)


def users_delete_confirmed_view(request, contato_id):
    Contato.objects.get(id=contato_id).delete()
    return HttpResponseRedirect(reverse('users:users'))


def users_edit_view(request, contato_id):
    if not request.user.is_authenticated:
        return render(request, 'libercom/home.html', {
            'message': 'Sem permissão para acessar esta página. Realize o login e tente novamente',
            'year': datetime.date.today().year,
        })

    contato = Contato.objects.get(id=contato_id)
    form = ContatoForm(request.POST or None, instance=contato)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('users:users'))

    context = {'form': form, 'contato_id': contato_id, 'year': datetime.date.today().year, 'option': 3}
    return render(request, "users/users-edit.html", context)


def users_new_view(request):
    if not request.user.is_authenticated:
        return render(request, 'libercom/home.html', {
            'message': 'Sem permissão para acessar esta página. Realize o login e tente novamente',
            'year': datetime.date.today().year,
        })

    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('users:users'))

    context = {'form': form, 'year': datetime.date.today().year, 'option': 3}
    return render(request, 'users/users-new.html', context)
