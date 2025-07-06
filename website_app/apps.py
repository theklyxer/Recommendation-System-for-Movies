from django.apps import AppConfig
import os
# from .utils import load_movie_data # Removed this import as it's no longer called here

class WebsiteAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'website_app'

    def ready(self):
        # Only run this logic if it's the main process (not the autoreloader process)
        if os.environ.get('RUN_MAIN', None) != 'true':
            print("Skipping app ready logic in autoreloader process.")
            return

        # Import the management command here to ensure apps are ready
        from django.core.management import call_command
        try:
            print("Attempting to call import_movie_data command...")
            call_command('import_movie_data')
            print("import_movie_data command finished.")
        except Exception as e:
            print(f"Error importing movie data: {e}")
        
        print("App ready method finished. Data loading for in-memory cache will happen lazily in views.")
