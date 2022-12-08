from django.urls import path
from .vistas.familiar_view import familiar_View

urlpatterns =[
    path('autogenerador_listar_fammiliares', familiar_View.autogenerar_listar_familiares)
]