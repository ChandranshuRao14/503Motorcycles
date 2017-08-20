import django_filters
from django import forms
from django.db.models import Q
from django_filters import FilterSet

from .models import Motorcycle

def createTuple(attr):
    resultMap = map(str,list(Motorcycle.objects.values_list(attr,flat=True).distinct()))
    newList = []
    for item in resultMap:
        newList.append((item,item))
    return tuple(newList)

MAKE_CHOICES = createTuple("make")

COLOR_CHOICES = createTuple("color")

YEAR_CHOICES = createTuple("year")

TYPE_CHOICES = createTuple("typeOfBike")

ESIZE_CHOICES = createTuple("engineSize")

def myFilter(queryset, name, value):
    if ' ' in value:
        vals = value.split(" ")
        return queryset.filter(Q(make__icontains=vals[0]) | Q(model__icontains=vals[0]) | Q(make__icontains=vals[1]) | Q(model__icontains=vals[1]))
    else:
        return queryset.filter(Q(make__icontains=value) | Q(model__icontains=value))

class MotoFilter(FilterSet):
    bike = django_filters.CharFilter(method=myFilter)
    make = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple, choices=MAKE_CHOICES)
    color = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple, choices=COLOR_CHOICES)
    year = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple, choices=YEAR_CHOICES)
    engineSize = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple, choices=ESIZE_CHOICES)
    typeOfBike = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple, choices=TYPE_CHOICES)
    mileage = django_filters.RangeFilter()
    price = django_filters.RangeFilter()

    class Meta:
        model = Motorcycle
        fields = ['make', 'model', 'color', 'year', 'engineSize', 'typeOfBike', 'antiLockBrakes', 'mileage','price']
