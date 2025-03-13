from django.contrib import admin
from .models import ServiceCategory, SalonService, MassageService, LaundryService, LaundryItem

class SalonServiceInline(admin.TabularInline):
    model = SalonService
    extra = 1

class MassageServiceInline(admin.TabularInline):
    model = MassageService
    extra = 1

class LaundryServiceInline(admin.TabularInline):
    model = LaundryService
    extra = 1

class LaundryItemInline(admin.TabularInline):
    model = LaundryItem
    extra = 1

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name', 'description')
    inlines = [SalonServiceInline, MassageServiceInline, LaundryServiceInline]

@admin.register(SalonService)
class SalonServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_minutes', 'is_active')
    search_fields = ('name', 'description')
    list_filter = ('is_active',)

@admin.register(MassageService)
class MassageServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_minutes', 'is_active')
    search_fields = ('name', 'description')
    list_filter = ('is_active',)

@admin.register(LaundryService)
class LaundryServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_type', 'price_per_kg', 'is_active')
    search_fields = ('name', 'description')
    list_filter = ('order_type', 'is_active')
    inlines = [LaundryItemInline]

@admin.register(LaundryItem)
class LaundryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_item', 'laundry_service', 'is_active')
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'laundry_service')