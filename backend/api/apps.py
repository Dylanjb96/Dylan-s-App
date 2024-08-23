from django.apps import AppConfig

# Define the configuration class for the 'api' application.
class ApiConfig(AppConfig):
    # Specify the default type of auto-generated primary key fields.
    # This ensures that all models in this app use 'BigAutoField' by default,
    # which is a 64-bit integer for primary keys, offering a larger range than the default IntegerField.
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Set the name of the application.
    # This is used by Django to identify this app and its configuration.
    name = 'api'

