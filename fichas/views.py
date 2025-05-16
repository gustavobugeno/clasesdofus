from django.shortcuts import render

def index(request):
    return render(request, 'fichas/index.html')

def detalle_ocra(request):
    return render(request, 'fichas/detalleocra.html')

def detalle(request):
    return render(request, 'fichas/detalle.html')
