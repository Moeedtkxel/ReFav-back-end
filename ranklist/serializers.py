from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.exceptions import *
from .models import RankList


class RankListSerializer(serializers.ModelSerializer):
    entry_name = serializers.CharField(source="entry.name", read_only=True)
    entry_owner = serializers.IntegerField(source="entry.owner_id", read_only=True)
    time = serializers.CharField(source='get_date')
    are_friendsornot = serializers.IntegerField(source='are_friends')
    if are_friendsornot is 1:
        raise serializers.ValidationError('This field must be an even number.')

    class Meta:
        model = RankList
        fields = [
            'id',
            'opinionname',
            'positionindex',
            'creator_id',
            'entry_id',
            'created_at',
            'entry_owner',
            'entry_name',
            'time',
            'are_friendsornot',
        ]

    read_only_fields = ['entry_id',
                        'created_at',
                        'entry_owner',
                        'entry_name',
                        'time',
                        ]

    def validate(self, data):
        # if self.are_friendsornot is not 1:
        return Response(status=status.HTTP_404_NOT_FOUND)