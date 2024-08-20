from django.shortcuts import redirect, render
from .forms import newUserForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
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

@login_required
def profile(request):
    return render(request, 'users/profile.html')


def create_profile(request):
    if request.method == 'POST':
        contact_no = request.POST.get('contact_no')
        image = request.FILES['upload']
        user = request.user
        profile = Profile(user = user, image=image, contact_no = contact_no )
        profile.save()

    return render(request, 'users/createprofile.html')


def seller_profile(request , id):
    seller = User.objects.get(id=id)
    context = {
        'seller': seller,
    }

    return render(request, 'users/sellerprofile.html',context)