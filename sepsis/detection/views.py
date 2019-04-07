from django.shortcuts import render
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from detection.models import Sepsis,Query
from detection.forms import Sepsisform,Query_form


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Create your views here.
def sepsis(request):
    title = "Sepsis Detection"
    if request.method == 'POST':
        form = Sepsisform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = Sepsisform()

    context = {"title": title, "form": form}
    return render(request, 'detection/form.html', context)



def query_create(request):
    title = "Query"
    if request.method == 'POST':
        form = Query_form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = Query_form()

    context = {"title": title, "form": form}
    return render(request, 'detection/form.html', context)





