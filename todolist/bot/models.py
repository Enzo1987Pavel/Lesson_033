from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.crypto import get_random_string


class TgUser(models.Model):
    tg_chat_id = models.BigIntegerField(verbose_name = "Telegram chat_id")
    tg_user_id = models.BigIntegerField(unique=True, verbose_name="Telegram user_id")
    tg_username = models.CharField(max_length=32, validators=[MinLengthValidator(5)], verbose_name="Пользователь Telegram")
    user = models.ForeignKey("core.User", null=True, blank=True, on_delete=models.CASCADE, verbose_name="Имя пользователя")
    verification_code = models.CharField(max_length=15, unique=True, verbose_name="Код верификации")

    def generate_verification_code(self) -> str:
        # chars = "sdfsdfsdf"  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # return get_random_string(15, chars)

        code = get_random_string(15)
        self.verification_code = code
        self.save()
        return code
