import csv
from django.core.management.base import BaseCommand
from website_app.models import MovieData
import pandas as pd

class Command(BaseCommand):
    help = 'Imports movie data from maindata_exp.csv into the MovieData model if the database is empty.'

    def handle(self, *args, **options):
        # Check if MovieData already exists in the database. If so, skip import.
        # NOTE: If you need to re-import data (e.g., after changing the source CSV),
        #       you must first clear the MovieData table manually (e.g., MovieData.objects.all().delete() in shell).
        if MovieData.objects.exists():
            self.stdout.write(self.style.SUCCESS('MovieData already exists in the database. Skipping import.'))
            return

        csv_file_path = 'website_app/static/csv_files/maindata_exp.csv' # Changed path
        try:
            df = pd.read_csv(csv_file_path)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Error: CSV file not found at {csv_file_path}'))
            return

        movies_to_create = []
        for index, row in df.iterrows():
            # Ensure we are only taking data for the model fields: movieid, title, tags
            movie = MovieData(
                movieid=row['movieid'],
                title=row['title'],
                tags=row['tags']
            )
            movies_to_create.append(movie)
        
        MovieData.objects.bulk_create(movies_to_create, ignore_conflicts=True)

        self.stdout.write(self.style.SUCCESS('Successfully imported movie data from maindata_exp.csv.')) 