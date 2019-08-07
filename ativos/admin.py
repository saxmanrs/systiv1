from django.contrib import admin
from .models import Ativos
from .models import TipoAtivo
from .models import Setor
from .models import StatusAtivo


# Register your models here.


admin.site.register(Ativos)
admin.site.register(TipoAtivo)
admin.site.register(Setor)
admin.site.register(StatusAtivo)