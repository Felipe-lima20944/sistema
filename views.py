from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

def my_login_view(request):
    if request.method == 'POST':
        # Limpar a sessão antes de fazer login para garantir apenas uma autenticação por sessão
        request.session.flush()

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('nova_view')
        else:
            messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required
def nova_view(request):
    return render(request, 'index.html')

@login_required
def sistema_view(request):
    # Aqui você pode adicionar lógica adicional, se necessário
    return render(request, 'sistema.html')

@login_required
def sistema2_view(request):
    return render(request, 'sistema2.html')


@login_required
def sistema3_view(request):
    return render(request, 'sistema3.html')
