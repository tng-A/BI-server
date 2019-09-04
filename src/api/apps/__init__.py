from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'src.api'

    def ready(self):
        from src.api.jobs import job
        job.start()
