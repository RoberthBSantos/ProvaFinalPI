from rest_framework import serializers, status
import random
import string

from rest_framework.response import Response

from links.models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['original', 'encurtado']
        read_only_fields = ['encurtado']

    def create(self, validated_data):
        encurtado = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(
            string.ascii_letters)
        link = Link.objects.create(original=validated_data.pop('original'), encurtado=encurtado)
        if (len(link.encurtado) > len(link.original)):
            # return Response({'error': 'não foi possível encurtar a url por ela ja ser menor que a url encurtada pelo sistema.'}, status=status.HTTP_400_BAD_REQUEST)
            raise serializers.ValidationError(
                {'error': 'não foi possível encurtar a url por ela ja ser menor que a url encurtada pelo sistema.'})
        return link


class LinkDesencurtadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['original']
