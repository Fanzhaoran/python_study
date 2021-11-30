import json

from django.shortcuts import render

from django.http import HttpResponse,JsonResponse
# Create your views here.


def bugInfo(request):

    return JsonResponse({'a':[1,2]})