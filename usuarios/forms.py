from django.forms import ModelForm
from .models import Usuarios

class UsuariosForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nome', 'nome_usuario','email', 'data_inicio', 'data_fim', 'setor', 'ramal']

