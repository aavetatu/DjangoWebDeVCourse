from django.apps import AppConfig
from .templatetags.custom_tags import register

class JournalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'journal'
