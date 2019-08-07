from django.forms import ModelForm
from .models import Ativos

class AtivosForm(ModelForm):
    class Meta:
        model = Ativos
        fields = ['sigla_ativo', 'tipo_ativo','marca_ativo', 'setor_ativo', 'data_fim', 'status_ativo', 'data_cadastro']

