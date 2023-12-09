from rest_framework import serializers
from .models import Proyek


class ProyekSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proyek
        fields = ['nama', 'category', 'tanggal', 'client', 'output', 'gambar']
