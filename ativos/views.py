from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from .models import Ativos
from .forms import AtivosForm

# Create your views here.





@login_required
def ativos_list(request):
    ativosdb = Ativos.objects.all()
    return render(request, 'ativos.html', {'ativos':ativosdb})




@login_required
def ativos_new(request):
    form = AtivosForm(request.POST or None, request.FILES or None)


    if form.is_valid():
        form.save()
        return redirect ('ativos_list')
    return render (request, 'ativos_frm.html',{'form': form})


@login_required
def ativos_upd(request, id):
    ativos = get_object_or_404(Ativos, pk=id)
    form = AtivosForm(request.POST or None, request.FILES or None, instance=ativos)

    if form.is_valid():
        form.save()
        return redirect('ativos_list')
    return render (request, 'ativos_frm.html',{'form': form})


@login_required
def usuarios_del(request, id):
    ativos = get_object_or_404(Ativos, pk=id)
    form = AtivosForm(request.POST or None, request.FILES or None, instance=ativos)

    if request.method=='POST':
        ativos.delete()    
        return redirect('ativos_list')
    return render (request, 'ativos_frm.html',{'form': form})

