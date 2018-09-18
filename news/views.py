# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import Pick
from .serializer import PickSerializer

from django.shortcuts import render

# Create your views here.

class PickViewSet(viewsets.ModelViewSet):
    queryset = Pick.objects.all()
    serializer_class = PickSerializer
