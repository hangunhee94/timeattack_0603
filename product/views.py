from django.shortcuts import render
from . models import Drink, Category
# Create your views here.
def choice_view(request):
    if request.method == 'GET':
        menu_list = Drink.objects.all()
        return render(request, 'product/menu_list.html', {'menu_list': menu_list})