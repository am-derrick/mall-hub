from rest_framework import serializers
from .models import ServiceCategory, SalonService, MassageService, LaundryService, LaundryItem

class SalonServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonService
        fields = ['id', 'name', 'description', 'price', 'duration_minutes', 'is_active']

class MassageServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MassageService
        fields = ['id', 'name', 'description', 'price', 'duration_minutes', 'is_active']

class LaundryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaundryItem
        fields = ['id', 'name', 'description', 'price_per_item', 'is_active']

class LaundryServiceSerializer(serializers.ModelSerializer):
    items = LaundryItemSerializer(many=True, read_only=True)

    class Meta:
        model = LaundryService
        fields = ['id', 'name', 'order_type', 'description', 'price_per_kg', 'is_active', 'items']


class ServiceCategorySerializer(serializers.ModelSerializer):
    salon_services = SalonServiceSerializer(many=True, read_only=True)
    massage_services = MassageServiceSerializer(many=True, read_only=True)
    laundry_services = LaundryServiceSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceCategory
        fields = ['id', 'name', 'description', 'icon', 'is_active', 'salon_services',
                  'massage_services', 'laundry_services']