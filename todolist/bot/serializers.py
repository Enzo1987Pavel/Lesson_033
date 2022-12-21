from rest_framework import serializers

from bot.models import TgUser


class TgUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        read_only_fields = ("tg_id", "tg_user_id")
        fields = ("verification_code",)
