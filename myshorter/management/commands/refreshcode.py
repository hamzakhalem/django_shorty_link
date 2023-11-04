from django.core.management.base import BaseCommand, CommandError
from myshorter.models import ShortyUrl


class Command(BaseCommand):
    help = "Refresh all short codes"
    def add_arguments(self, parser):
        parser.add_argument("number", nargs="+", type=int)

    def handle(self, *args, **options):
        ShortyUrl.objects.refresh_shortcodes(items=options['number'][0])