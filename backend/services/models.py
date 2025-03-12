from django.db import models

class ServiceCategory(models.Model):
    """
    YOM service categories: Salon, Massage, Laundry
    These are shown on the customer dashboard at the top level
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="CSS class name for icon")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Service Categories"


class SalonService(models.Model):
    """
    Salon services like haircuts, manicure, pedicures, etc.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    duration_minutes = models.IntegerField(default=30)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='salon_services')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} (${self.price})"
    

class MassageService(models.Model):
    """
    Class containing massage services like Deep Tissue, Swedish etc.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    duration_minutes = models.IntegerField(default=60)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='massage_services')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} (${self.price})"
    

class LaundryService(models.Model):
    """
    Class for laundry services based on types
    """
    ORDER_TYPE_CHOICES = (
        ('by_weight', 'By Weight'),   # e.g. load wash
        ('by_items', 'By Items'),     # e.g. suits, duvets etc..
    )

    name = models.CharField(max_length=100)
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE_CHOICES)
    description = models.TextField(blank=True)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='laundry_services')
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.get_order_type_display()})"
    

class LaundryItem(models.Model):
    """
    Individual laundry itesm for 'by_items' order type 
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=0)
    laundry_service = models.ForeignKey(LaundryService, on_delete=models.CASCADE, related_name='items')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} (${self.price_per_item})"