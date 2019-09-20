from rest_framework import viewsets
from api.band.models import Band
from api.band.serializers import BandSerializer


class BandViewSet(viewsets.ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

