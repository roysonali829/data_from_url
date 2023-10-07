from django.shortcuts import render
from datetime import datetime

# Create your views here.

def build_in_filters(request):
    data = 'hAi HEllo How aRe YOU'
    dt = datetime.now()
    d = {'data':data,'dt':dt,'c':1}
    return render(request,'build_in_filters.html',d)


def usd_filters(request):
    d = {'data':'hAi Python'}
    return render(request,'usd_filters.html',d)