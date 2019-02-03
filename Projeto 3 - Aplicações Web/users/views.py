from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Faz o cadastro de um novo usuário."""

    if request.method != 'POST':
        # Exibe o formulário em branco
        form = UserCreationForm()
    else:
        # Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            # Faz login do usuário e o redireciona para a página inicial
            authenticated_user = authenticate(username=new_user.username,
                                            password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    
    context = {'form': form}
    return render(request, 'users/register.html', context)


#       Se os dados submetido forem válidos, chamamos o método 'save()' do
#       formulário para salvar o nome do usuário e a hash da senha no banco de
#       dados. O método 'save()' devolve um objeto para o usuário recém-criado,
#       que armazenamos em 'new_user'.
#
#       Quando as informações forem salvas, fazemos o seu login, que é um processo
#       de dois passos: chamamos 'authenticate()' com os argumentos 'username' e
#       'password'. Nesse caso, lemos o valor associado à chave 'password1' nos
#       dados de POST do formulário. Se as credenciais estiverem corretas, o método
#       devolverá um objeto com o usuário autenticado, que armazenamos em
#       'authenticated_user'. Então chamamos a função 'login()' com os objetos
#       'request' e 'authenticated_user' que criará uma sessão válida para o
#       usuário.