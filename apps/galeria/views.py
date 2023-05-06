from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages
from apps.galeria.forms import FotografiaForms

def autenticacao_requerida(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Usuário não logado')
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

@autenticacao_requerida
def index(request):
    fotografia = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografia})

@autenticacao_requerida
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

@autenticacao_requerida
def buscar(request):
    fotografia = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografia = fotografia.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/index.html', {"cards": fotografia})

@autenticacao_requerida
def nova_imagem(request):
    form = FotografiaForms
    if request.method == 'POST': # verifica se foi enviado algo 
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save() # salva no banco de dados
            messages.success(request, 'Nova fotografia cadastrada!!')
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {'form': form})

@autenticacao_requerida
def editar_imagem(request,foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save() # salva no banco de dados
            messages.success(request, 'Fotografia editada com sucesso!!')
            return redirect('index')

    return render (request, 'galeria/editar_imagem.html', {'form':form, 'foto_id': foto_id})

@autenticacao_requerida
def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Deleção feita com sucesso')
    return redirect('index')

def filtro(request, categoria):
    if categoria == "TODOS":
        fotografia = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
        return render(request, "galeria/index.html", {"cards": fotografia})

    fotografia = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria )
    return render(request, "galeria/index.html", {"cards": fotografia})
