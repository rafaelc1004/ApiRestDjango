from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def api(request):
    body = {
        'nombre':'rafael',
        'apellido':'castillo',
        'telefono':'989641620',
    }
    return JsonResponse(body)
    