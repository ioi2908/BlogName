from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'registration'

    def ready(self):
        import registration.signals

