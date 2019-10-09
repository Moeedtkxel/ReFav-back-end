# Create your views here.
from rest_framework import generics

from .models import RankList
from .serializers import RankListSerializer


class DisplayAllRankLists(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = RankListSerializer
    queryset = RankList.objects.all()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return RankList.objects.all()
        else:
            return RankList.objects.all().filter()

class RankListViaURL(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = RankListSerializer

    def get_queryset(self):
        return RankList.objects.filter(entry_id=self.request.query_params.get("entry_id"))