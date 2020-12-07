from django.core.management.base import BaseCommand
from prodapp.models import Category, SubCategory


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        SubCategory.objects.all().delete()
