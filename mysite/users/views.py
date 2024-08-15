from django.shortcuts import redirect, render
from .forms import newUserForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = newUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('myapp/products')

    form = newUserForm()
    context={
        'form': form,
    }

    return render(request,'users/register.html', context)