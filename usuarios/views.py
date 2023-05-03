from django.shortcuts import render, redirect
<<<<<<< HEAD
=======

>>>>>>> desenvolvendo
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages 

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
<<<<<<< HEAD
        
        usuario = auth.authenticate( # faz a autenticação do usuario,biblioteca do django
            request,
            username = nome,
            password = senha
        )
        if usuario is not None:
            auth.login(request,usuario)
            messages.success(request,f'{nome}, logado com sucesso!!')
            return redirect('index')
        else:
            messages.error(request,'Erro ao efetuar o login')
            return redirect('login')

    return render(request, "usuarios/login.html", {'form' : form})
=======

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!'.capitalize())
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})
>>>>>>> desenvolvendo

def cadastro(request):
    form = CadastroForms()

<<<<<<< HEAD
    if request.method == "POST":
=======
    if request.method == 'POST':
>>>>>>> desenvolvendo
        form = CadastroForms(request.POST)

        if form.is_valid():

<<<<<<< HEAD
            if form['senha_1'].value() != form['senha_2'].value(): # dessa forma conseguimos buscas os valores de uma resposta no formulario!!
                messages.error(request, 'Senhas não são iguais')
                return redirect('cadastro')  # serve para redirecionar a pagina desejada que nesse caso seria cadastro

            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha= form["senha_1"].value()

            if User.objects.filter(username=nome,).exists(): # verificar se o usuario ja existe
                messages.error(request, 'usuario ja existente')
                return redirect('cadastro')
            elif User.objects.filter(email__iexact=email).exists():
                messages.error(request, 'usuario ja existente')
                return redirect('cadastro')

            usuario = User.objects.create_user( #cria o usuario
                username=nome,
                email= email,
                password= senha
            )
            usuario.save()
            messages.success(request,f'{nome}, obrigado por se cadastrar')
            return redirect('login')

    return render(request, "usuarios/cadastro.html", {'form' : form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso')
=======
            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro')
            elif User.objects.filter(email__iexact=email).exists():
                    messages.error(request, 'Usuário já existente')
                    return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
>>>>>>> desenvolvendo
    return redirect('login')