from django.shortcuts import render
from django.http import HttpResponse
from sklearn.ensemble import RandomForestRegressor
import pickle
import numpy as np

# Create your views here.

def index(request):
    # Page from the theme 
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def rent_calculator(request):
    if "GET" == request.method:
        return render(request, 'pages/rent-calculator.html')
    else:
        model = pickle.load(open('trainedmodels/trained_model.pkl', 'rb'))
        district = request.POST.get("district")
        area = request.POST.get("area")
        bed = request.POST.get("bed")
        bath = request.POST.get("bath")
        car = request.POST.get("car")
        cond = request.POST.get("cond")
        predict = int(np.around(model.predict([[district, area, cond]])[0], 0))
        context = {
            'result': predict,
            }
        return render(request, 'pages/rent-calculator.html', context)