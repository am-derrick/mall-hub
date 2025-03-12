from rest_framework import viewsets, permissions, filters
from .models import ServiceCategory, SalonService, MassageService, LaundryService, LaundryItem
from .serializers import (
    ServiceCategorySerializer, SalonServiceSerializer, MassageServiceSerializer,
    LaundryServiceSerializer, LaundryItemSerializer
)

class ServiceCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for service categories (Salon, Massage, Laundry)
    """
    queryset = ServiceCategory.objects.filter(is_active=True)
    serializer_class = ServiceCategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    def get_permissions(self):
        """
        Allow anyone to view, but only admin to modify
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    

class SalonServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for salon services
    """
    queryset = SalonService.objects.filter(is_active=True)
    serializer_class = SalonServiceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    def get_permissions(self):
        """
        Allow anyone to view, but only admin to modify
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        """
        Filter by category provided in query params
        """
        queryset = SalonService.objects.filter(is_active=True)
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset
    

class MassageServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for massage services
    """
    queryset = MassageService.objects.filter(is_active=True)
    serializer_class = MassageServiceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    def get_permissions(self):
        """
        Allow anyone to view, but only admin to modify
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        """
        Filter by category provided in query params
        """
        queryset = MassageService.objects.filter(is_active=True)
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset
    

class LaundryServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for laundry services
    """
    queryset = LaundryService.objects.filter(is_active=True)
    serializer_class = LaundryServiceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    def get_permissions(self):
        """
        Allow anyone to view, but only admin to modify
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        """
        Filter by category provided in query params
        """
        queryset = LaundryService.objects.filter(is_active=True)
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset
    

class LaundryItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for laundry items
    """
    queryset = LaundryItem.objects.filter(is_active=True)
    serializer_class = LaundryItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    def get_permissions(self):
        """
        Allow anyone to view, but only admin to modify
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        """
        Filter by category provided in query params
        """
        queryset = LaundryItem.objects.filter(is_active=True)
        service_id = self.request.query_params.get('service')
        if service_id:
            queryset = queryset.filter(laundry_service_id=service_id)
        return queryset