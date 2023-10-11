from django.forms import ModelForm
from app.models import Registro


class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        fields = ['n_do_protocolo', 'apresentante', 'status', 'codigo']






