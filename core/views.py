from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from core.models import Produto


def index(request):
    produtos = Produto.objects.all().order_by('-id')
    context = {'produtos': produtos}
    return render(request, 'core/pages/index.html', context )

def contato(request):
    return render(request, 'core/pages/contato.html')

def produto(request, id):
    #prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto, id=id)
    return render(request, 'core/pages/produto.html', {'produto': prod})

def error404(request, ex):
    template = loader.get_template('core/pages/404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=404 )

def error500(request):
    template = loader.get_template('core/pages/500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=500 )