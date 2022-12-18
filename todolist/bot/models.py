import random
import string

from django.db import models

from core.models import User


class TgUser(models.Model):
    class Meta:
        verbose_name = "Telegram Пользователь"
        verbose_name_plural = "Telegram Пользователи"

    tg_chat_id = models.BigIntegerField(verbose_name="tg_chat_id")
    tg_user_id = models.BigIntegerField(unique=True, verbose_name="tg_user_id")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, default=None)
    verification_code = models.CharField(max_length=12, unique=True)
    username = models.CharField(
        max_length=150,
        verbose_name="Telegram_username",
        null=True,
        blank=True,
        default=None
    )

    def set_verification_code(self) -> None:
        length = 12
        digits = string.digits
        v_code = ''.join(random.sample(digits, length))
        self.verification_code = v_code


