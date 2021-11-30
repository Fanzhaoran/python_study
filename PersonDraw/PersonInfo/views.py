from django.shortcuts import render

from .models import Person, Program, ProgramInFo
import json
from rest_framework import viewsets
from .serializers import PersonSerializer, ProgramSerializer, PersonItemSerializer


# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramInfoViewSet(viewsets.ModelViewSet):
    queryset = ProgramInFo.objects.all()
    serializer_class = PersonItemSerializer


