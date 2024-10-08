from django.shortcuts import render
from rest_framework import viewsets, pagination, status
from rym.pagination import CustomPagination
from rym.filters import CharacterFilter, LocationFilter
from rym.models import *
from rym.serializers import *
from filter_and_pagination import FilterPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

# Models viewsets 
class LocationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LocationFilter
    
class EpisodeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

    
class CharacterViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CharacterFilter
    pagination_class = CustomPagination
    
