from django.db import models


class TgUser(models.Model):
    class Meta:
        verbose_name = "Telegram пользователь"
        verbose_name_plural = "Telegram пользователи"

    tg_id = models.BigIntegerField(verbose_name="tg_id", unique=True)
    tg_chat_id = models.BigIntegerField(verbose_name="tg_chat_id")
    username = models.CharField(max_length=256, verbose_name="tg_username", null=True, blank=True, default=None)
    user = models.ForeignKey("core.User", models.PROTECT, null=True, blank=True, default=None, verbose_name="Пользователь")
