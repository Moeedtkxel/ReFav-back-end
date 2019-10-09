from rest_framework import serializers
from .models import RankList


class RankListSerializer(serializers.ModelSerializer):
    entry_name = serializers.CharField(source="entry.name", read_only=True)
    entry_owner = serializers.IntegerField(source="entry.owner_id", read_only=True)
    time = serializers.CharField(source='get_date')

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
        ]

    read_only_fields = ['entry_id',
                        'created_at',
                        'entry_owner',
                        'entry_name',
                        'time', ]
