from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuarios
from .forms import UsuariosForm


@login_required
def usuarios_list (request):
    usuariosdb = Usuarios.objects.all()
    return render(request,'usuarios.html',{'users': usuariosdb })



@login_required
def usuarios_new(request):
    form = UsuariosForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('usuarios_list')
    return render (request, 'usuarios_frm.html',{'form': form})



@login_required
def usuarios_upd(request, id):
    usuarios = get_object_or_404(Usuarios, pk=id)
    form = UsuariosForm(request.POST or None, request.FILES or None, instance=usuarios)

    if form.is_valid():
        form.save()
        return redirect('usuarios_list')
    return render (request, 'usuarios_frm.html',{'form': form})


@login_required
def usuarios_del(request, id):
    usuarios = get_object_or_404(Usuarios, pk=id)
    form = UsuariosForm(request.POST or None, request.FILES or None, instance=usuarios)

    if request.method=='POST':
        usuarios.delete()    
        return redirect('usuarios_list')
    return render (request, 'usuarios_del_conf.html',{'form': form})


