from django.core.management.base import BaseCommand
from webapp.utilities.emailing.emailing import emailing


class Command(BaseCommand):

    def handle(self, *args, **options):
        emailing()
