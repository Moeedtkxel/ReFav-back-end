# Create your views here.
from rest_framework import generics

from .models import Categories
from .serializers import CategorySerializer


class DisplayAllCategories(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CategorySerializer
    queryset = Categories.objects.all()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Categories.objects.all()
        else:
            return Categories.objects.all().filter()
