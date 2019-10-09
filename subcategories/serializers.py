from rest_framework import serializers
from .models import SubCategories


class SubCategorySerializer(serializers.ModelSerializer):
    parent_category_name = serializers.CharField(source="parent_category.name", read_only=True)

    class Meta:
        model = SubCategories
        fields = [
            'id',
            'name',
            'parent_category',
            'parent_category_name',
        ]
