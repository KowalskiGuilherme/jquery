from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Empresa
from .forms import EmpresaForm


def save_empresa_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            empresas = Empresa.objects.all()
            data['html_empresa_list'] = render_to_string('empresa/includes/partial_empresa_list.html', {
                'empresas': empresas
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def empresa_create(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
    else:
        form = EmpresaForm()
    return save_empresa_form(request, form, 'empresa/includes/partial_empresa_create.html')


def empresa_update(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
    else:
        form = EmpresaForm(instance=empresa)
    return save_empresa_form(request, form, 'empresa/includes/partial_empresa_update.html')


def empresa_list(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresa/empresa_list.html', {'empresas': empresas})