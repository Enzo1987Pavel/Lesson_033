from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.crypto import get_random_string


class TgUser(models.Model):
    class Meta:
        verbose_name = "Пользователь Telegram"
        verbose_name_plural = "Пользователи Telegram"

    tg_chat_id = models.BigIntegerField(verbose_name="tg_chat_id")
    tg_user_id = models.BigIntegerField(unique=True, verbose_name="tg_user_id")
    tg_username = models.CharField(max_length=32, validators=[MinLengthValidator(5)], verbose_name="tg_username")
    user = models.ForeignKey("core.User", null=True, blank=True, on_delete=models.CASCADE, verbose_name="Имя пользователя")
    verification_code = models.CharField(max_length=15, unique=True, verbose_name="Код верификации")

    def generate_verification_code(self) -> str:
        # chars = "sdfsdfsdf"  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # return get_random_string(15, chars)

        code = get_random_string(15)
        self.verification_code = code
        self.save()
        return code
