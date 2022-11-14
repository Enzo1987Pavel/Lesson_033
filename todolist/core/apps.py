from django.apps import AppConfig

VERBOSE_APP_NAME = "Домашка #33"


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = VERBOSE_APP_NAME
