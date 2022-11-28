from django.apps import AppConfig

VERBOSE_APP_NAME = "Дипломный проект"


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
    verbose_name = VERBOSE_APP_NAME
