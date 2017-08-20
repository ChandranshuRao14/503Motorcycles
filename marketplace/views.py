from django.views import generic
from .models import Motorcycle
from django.shortcuts import render
from .filters import MotoFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404

def index(request):
    bike_list = Motorcycle.objects.all()
    # moto_filter = MotoFilter(request.GET, queryset=bike_list)
    # paginator = Paginator(moto_filter.qs, 5)
    # page = request.GET.get('page')
    # try:
    #     bikes = paginator.page(page)
    # except PageNotAnInteger:
    #     bikes = paginator.page(1)
    # except EmptyPage:
    #     bikes = paginator.page(paginator.num_pages)

    return render(request, 'marketplace/index.html', context = {'bikes': bikes}) #{'filter': moto_filter,'bikes': bikes})

def detail(request, pk):
    form = ContactForm()
    motorcycle = Motorcycle.objects.get(pk=pk)
    return render(request, 'marketplace/detail.html', {'form': form, 'motorcycle': motorcycle})