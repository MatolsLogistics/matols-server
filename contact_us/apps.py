from django.apps import AppConfig


class ContactUsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact_us'

        # ready 
    def ready(self) -> None:
        import contact_us.signals
