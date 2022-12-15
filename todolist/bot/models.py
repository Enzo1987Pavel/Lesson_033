from django.db import models

import random
import string

from core.models import User


class TgUser(models.Model):
    class Meta:
        verbose_name = 'TG User'
        verbose_name_plural = 'TG Users'

    tg_chat_id = models.BigIntegerField(verbose_name='TG CHAT_ID')
    tg_user_id = models.BigIntegerField(unique=True, verbose_name='TG USER_ID')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, default=None)
    username = models.CharField(max_length=255, null=True, blank=True, default=None, verbose_name='TG USERNAME')
    verification_code = models.CharField(max_length=12, unique=True)

    def set_verification_code(self) -> None:
        length = 12
        digits = string.digits
        v_code = ''.join(random.sample(digits, length))
        self.verification_code = v_code
