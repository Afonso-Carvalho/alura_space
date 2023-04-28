from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de login',
        required=True,
        max_length=100,
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Ex.: Afonso Xavier'
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', #formatação
                'placeholder':'Ex.: Digite sua senha'
            }
        ),#ficar pontilhado
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de login',
        required=True,
        max_length=100,
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Ex.: Afonso Xavier'
            }
        )
    )
    email= forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Ex.: afonsoxavier@gmail.com'
            }
        )
    )
    senha_1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', #formatação
                'placeholder':'Ex.: Digite sua senha'
            }
        ),#ficar pontilhado
    )
    senha_2 = forms.CharField(
        label='Confirme sua senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', #formatação
                'placeholder':'Ex.: Digite sua senha novamente'
            }
        ),#ficar pontilhado
    )
