from django.apps import AppConfig

VERBOSE_APP_NAME = "Список досок и категорий"


class GoalsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "goals"
    verbose_name = VERBOSE_APP_NAME
