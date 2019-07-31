from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm


@login_required
def produto_list(request):
    produtosbd = Produto.objects.all()
    return render(request, 'produto.html', {'products': produtosbd})


@login_required
def produto_new(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('produto_list')
    return render(request, 'produto_frm.html', {'form': form})


@login_required
def produto_upd(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('produto_list')
    return render(request, 'produto_frm.html', {'form': form})


@login_required
def produto_del(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)

    if request.method == 'POST':
        produto.delete()
        return redirect('produto_list')
    return render(request, 'produto_del_conf.html', {'form': form})


