from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.crypto import get_random_string


class TgUser(models.Model):
    class Meta:
        verbose_name = "Пользователь Telegram"
        verbose_name_plural = "Пользователи Telegram"

    tg_chat_id = models.BigIntegerField(verbose_name="id чата")
    tg_user_id = models.BigIntegerField(unique=True, verbose_name="id позьзователя")
    tg_username = models.CharField(max_length=32, validators=[MinLengthValidator(5)], verbose_name="Имя позьзователя")
    user = models.ForeignKey("core.User", null=True, blank=True, on_delete=models.CASCADE, verbose_name="Позьзователь приложения")
    verification_code = models.CharField(max_length=15, unique=True, verbose_name="Код верификации")

    def generate_verification_code(self) -> str:
        code = get_random_string(15)
        self.verification_code = code
        self.save()
        return code