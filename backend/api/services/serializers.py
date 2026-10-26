from rest_framework import serializers

from apps.services.models import Category, Feature, Service
from apps.portfolio.models import Technology


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    features = FeatureSerializer(many=True, read_only=True)
    technologies = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = "__all__"

    def get_technologies(self, obj):
        return [
            {
                "id": technology.id,
                "name": technology.name,
                "category": technology.category,
            }
            for technology in obj.technologies.filter(active=True)
        ]