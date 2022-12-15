import random
import string

from django.db import models
from core.models import User

VERIFICATION_CODE_VOCABULARY = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


class TgUser(models.Model):
    class Meta:
        verbose_name = "Telegram пользователь"
        verbose_name_plural = "Telegram пользователи"

    tg_chat_id = models.BigIntegerField(verbose_name="tg_chat_id")
    tg_user_id = models.BigIntegerField(verbose_name="tg_user_id", unique=True)
    username = models.CharField(max_length=150, verbose_name="tg_username", null=True, blank=True, default=None)
    user = models.ForeignKey(User, models.PROTECT, null=True, blank=True, default=None, verbose_name="Пользователь")
    verification_code = models.CharField(max_length=12, unique=True, verbose_name="Код подтверждения")
    #
    # def set_verification_code(self):
    #     code = "".join([random.choice(VERIFICATION_CODE_VOCABULARY) for _ in range(12)])
    #     self.verification_code = code

    def set_verification_code(self) -> None:
        length = 8
        digits = string.digits
        v_code = "".join(random.sample(digits, length))
        self.verification_code = v_code
