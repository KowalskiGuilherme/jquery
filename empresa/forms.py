from django import forms
from django.utils.translation import ugettext_lazy as _
from empresa.models import Empresa


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('title', 'verba', 'group')
        labels = {'title': _('Nome'),
                  }

