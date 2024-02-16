from django.core.management.base import BaseCommand
from generation.models import Generation

class Command(BaseCommand):
    help = 'manage video objects'
    def handle(self, *args, **options):
        generations_data = [
            {'number': 6, 'suffix': 'th'},
            {'number': 7, 'suffix': 'th'},
            {'number': 8, 'suffix': 'th'},
            {'number': 9, 'suffix': 'th'},
            {'number': 10, 'suffix': 'th'},
            {'number': 11, 'suffix': 'th'},
            {'number': 12, 'suffix': 'th'},
        ]

        for gen_data in generations_data:
            Generation.objects.create(**gen_data)

        self.stdout.write(self.style.SUCCESS('Generation data created!'))
