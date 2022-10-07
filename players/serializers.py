from rest_framework import serializers
from players.models import Players

class playersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ('id', 'name', 'password', 'score')
