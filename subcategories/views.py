# Create your views here.
from rest_framework import generics

from .models import SubCategories
from .serializers import SubCategorySerializer


class DisplayAllSubCategories(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = SubCategorySerializer
    queryset = SubCategories.objects.all()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return SubCategories.objects.all()
        else:
            return SubCategories.objects.all()
