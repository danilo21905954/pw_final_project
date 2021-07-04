from django.urls import path

from . import views

app_name = 'libercom'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('plano/', views.plano_view, name='plano'),
    path('quizz/', views.quizz_view, name='quizz'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('contato/', views.add_page_view, name="adicionar"),
    path('success/', views.success_view, name="success"),
    path('sitemap/', views.sitemap_view, name="sitemap"),
    path('add/testemunho/', views.add_testemunho_view, name="add-testemunho"),
    path('add/testemunho/success', views.add_testemunho_success_view, name="add-testemunho-success")
]
