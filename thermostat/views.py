from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse

from .models import Reading
from .serializers import ReadingSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the thermostat index.")


class ReadingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
