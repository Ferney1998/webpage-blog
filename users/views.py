from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.decorators import login_required #para restringir vistas a usuarios no loggeados
from .forms import UserRegisterForm

def register(request):  #CAMBIAR A VISTA BASADA EN CLASE
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Now you can Log In!')
            return redirect('login')
            
    else:
        form = UserRegisterForm()     
    return render(request, 'users/register.html', {'form': form})

@login_required #decorador para requerir inicio de sesión para mostrar la vista
def profile(request):
    return render(request, 'users/profile.html')