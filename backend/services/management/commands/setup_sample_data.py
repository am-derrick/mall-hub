from django.core.management.base import BaseCommand
from services.models import ServiceCategory, SalonService, MassageService, LaundryService, LaundryItem

class Command(BaseCommand):
    help = 'Sets up sample data for the Services app'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample service data...')
        
        # Create service categories
        categories = {
            'Salon': 'Hair and beauty services for all your styling needs',
            'Massage': 'Relaxation and therapeutic massage services',
            'Laundry': 'Professional cleaning and laundry services'
        }
        
        created_categories = {}
        for name, desc in categories.items():
            cat, created = ServiceCategory.objects.get_or_create(
                name=name, 
                defaults={
                    'description': desc,
                    'icon': f'{name.lower()}-icon'  # Placeholder icon class
                }
            )
            created_categories[name] = cat
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f'{status}: Category "{name}"')
        
        # Create salon services
        salon_services = [
            {'name': 'Haircut', 'price': 20000, 'duration_minutes': 45, 
             'description': 'Professional haircut by our expert stylists'},
            {'name': 'Braiding', 'price': 100000, 'duration_minutes': 120,
             'description': 'Premium braids based on your desired needs and style'},
            {'name': 'Manicure', 'price': 10000, 'duration_minutes': 30,
             'description': 'Nail care and polish for beautiful hands'},
            {'name': 'Pedicure', 'price': 10000, 'duration_minutes': 45,
             'description': 'Foot care and nail polish for beautiful feet'},
            {'name': 'Facial', 'price': 250000, 'duration_minutes': 60,
             'description': 'Rejuvenating facial treatment for glowing skin'},
        ]
        
        for service in salon_services:
            obj, created = SalonService.objects.get_or_create(
                name=service['name'],
                category=created_categories['Salon'],
                defaults={
                    'price': service['price'],
                    'duration_minutes': service['duration_minutes'],
                    'description': service['description']
                }
            )
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f'{status}: Salon service "{service["name"]}"')
        
        # Create massage services
        massage_services = [
            {'name': 'Swedish Massage', 'price': 70000, 'duration_minutes': 60,
             'description': 'Gentle massage to relax and energize'},
            {'name': 'Deep Tissue', 'price': 85000, 'duration_minutes': 60,
             'description': 'Focused massage for chronic muscle tension'},
            {'name': 'Hot Stone', 'price': 95000, 'duration_minutes': 90,
             'description': 'Heated stones and massage for deep relaxation'},
            {'name': 'Aromatherapy', 'price': 80000, 'duration_minutes': 75,
             'description': 'Massage with essential oils for mind and body'},
            {'name': 'Sports Massage', 'price': 90000, 'duration_minutes': 60,
             'description': 'Targeted massage for athletes and active individuals'},
        ]
        
        for m_type in massage_services:
            obj, created = MassageService.objects.get_or_create(
                name=m_type['name'],
                category=created_categories['Massage'],
                defaults={
                    'price': m_type['price'],
                    'duration_minutes': m_type['duration_minutes'],
                    'description': m_type['description']
                }
            )
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f'{status}: Massage type "{m_type["name"]}"')
        
        # Create laundry services
        laundry_services = [
            {'name': 'Regular Washing', 'order_type': 'by_weight', 'price_per_kg': 2000,
             'description': 'Standard washing service charged by weight'},
            {'name': 'Premium Washing', 'order_type': 'by_weight', 'price_per_kg': 5000,
             'description': 'Premium washing with special detergents charged by weight'},
            {'name': 'Specialized Items', 'order_type': 'by_items', 'price_per_kg': None,
             'description': 'Specialized cleaning for specific items'},
        ]
        
        for ls in laundry_services:
            laundry_service, created = LaundryService.objects.get_or_create(
                name=ls['name'],
                category=created_categories['Laundry'],
                defaults={
                    'order_type': ls['order_type'],
                    'price_per_kg': ls['price_per_kg'],
                    'description': ls['description']
                }
            )
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f'{status}: Laundry service "{ls["name"]}"')
            
            # Create laundry items for the "by_items" service
            if ls['order_type'] == 'by_items' and created:
                items = [
                    {'name': 'T-Shirt', 'price_per_item': 2500, 
                     'description': 'Clean and press T-shirt'},
                    {'name': 'Pants/Trousers', 'price_per_item': 3500, 
                     'description': 'Clean and press pants or trousers'},
                    {'name': 'Dress', 'price_per_item': 5000, 
                     'description': 'Clean and press dress'},
                    {'name': 'Suit', 'price_per_item': 10000, 
                     'description': 'Clean and press complete suit'},
                    {'name': 'Jacket', 'price_per_item': 6000, 
                     'description': 'Clean and press jacket'},
                    {'name': 'Bedsheet', 'price_per_item': 4000, 
                     'description': 'Clean bedsheet'},
                    {'name': 'Towel', 'price_per_item': 5000, 
                     'description': 'Clean towel'},
                ]
                
                for item in items:
                    obj, created = LaundryItem.objects.get_or_create(
                        name=item['name'],
                        laundry_service=laundry_service,
                        defaults={
                            'price_per_item': item['price_per_item'],
                            'description': item['description']
                        }
                    )
                    self.stdout.write(f'Created: Laundry item "{item["name"]}"')
        
        self.stdout.write(self.style.SUCCESS('Sample data setup complete!'))