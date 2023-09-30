from django.urls import path

from apps.contato.views import index, view, editar

urlpatterns = [
    path('', index, name='index'),
    path('form', view, name='form'),
    path('editar/<int:id>', editar, name='editar'),
    # path('editar/<int:id>/', views.editar_campo, name='editar_campo'),
]