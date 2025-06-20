from django.shortcuts import render
from .forms import BookingForm
from .models import Menu

def menu(request):
    items = Menu.objects.all()
    return render(request, 'restaurant/menu.html', {'menu_items': items})

def home(request):
    return render(request, 'index.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)

def about(request):
    return render(request, 'about.html')
