from rest_framework import serializers

from bot.models import TgUser


class TgUserSerializer(serializers.ModelSerializer):
    class Meta:
        midel = TgUser
        fields = ("verification_code",)
