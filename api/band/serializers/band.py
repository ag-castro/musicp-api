from rest_framework.serializers import ModelSerializer
from api.band.models import Band


class BandSerializer(ModelSerializer):

    class Meta:
        model = Band
        fields = '__all__'
