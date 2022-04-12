from rest_framework import serializers
from .models import Subscription,metadata


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('id', 'name', 'description', 'currency',
            'amount', 'created_at', 'updated_at'
        )


class metadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = metadata
        fields = ('id','Location', 'Department', 'category', 'subcategory',
            'created_at', 'updated_at'
        )        