from django.apps import AppConfig

# Probably not needed for this simple app, but leaving as is from the Azure template
class HelloAzureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hello_azure'
