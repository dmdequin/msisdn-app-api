"""
Django command for populating the db using sample data.
"""
import csv
from django.core.management import BaseCommand

# Import the model
from core.models import MSISD


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from db_sample.csv"

    def handle(self, *args, **options):
        with open('./db_sample.csv') as file:
            reader = csv.reader(file)
            next(reader)  # Advance past the header

            if MSISD.objects.exists():
                print('MSISD data already loaded.')
                print('Deleting existing database...')
                MSISD.objects.all().delete()

            for row in reader:
                print('Reloading database...')
                print(row)

                msisd = MSISD(msisdn=row[0],
                              MNO=row[1],
                              country_code=row[2],
                              subscriber_number=row[3],
                              country_identifier=row[4])
                msisd.save()
