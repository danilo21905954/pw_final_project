from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', user_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('exit/', exit_view, name='exit'),

    path('quizz/', quizz_view, name='quizz'),

    path('statistics/', statistics_view, name='statistics'),
    path('char_data/', statistics_data, name='statistics_data'),


    path('testemunhos/', testemunho_view, name='testemunho'),
    path('testemunho-delete/<int:testemunho_id>', testemunho_delete_view, name='testemunho-delete'),
    path('testemunho-delete/confirmed/<int:testemunho_id>',
         testemunho_delete_confirmed_view, name='testemunho-delete-confirmed'),
    path('testemunho-edit/<int:testemunho_id>', testemunho_edit_view, name='testemunho-edit'),

    path('planos/', plano_view, name='planos'),
    path('planos/new/', plano_new_view, name='plano-new'),
    path('plano-edit/<int:plano_id>', plano_edit_view, name='plano-edit'),
    path('plano-delete/<int:plano_id>', plano_delete_view, name='plano-delete'),
    path('plano-delete/confirmed/<int:plano_id>', plano_delete_confirmed_view, name='plano-delete-confirmed'),


    path('users/', users_view, name='users'),
    path('users-delete/<int:contato_id>', users_delete_view, name='users-delete'),
    path('users-delete/confirmed/<int:contato_id>', users_delete_confirmed_view, name='users-delete-confirmed'),
    path('users-edit/<int:contato_id>', users_edit_view, name='users-edit'),
    path('users-new/', users_new_view, name='users-new'),
]
