from rest_framework import serializers

from .models import Reading


class ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reading
        fields = ('location', 'temperature', 'timestamp')
