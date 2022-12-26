from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from bot.models import TgUser


class TgUserSerializer(serializers.ModelSerializer):
    verification_code = serializers.CharField(write_only=True)

    class Meta:
        model = TgUser
        read_only_fields = ('id', 'tg_chat_id', 'tg_user_id', 'tg_username')
        fields = ('tg_chat_id', 'tg_user_id', 'tg_username', 'verification_code', 'user_id')

    def validate(self, attrs: dict) -> dict:
        verification_code = attrs.get('verification_code')
        tg_user = TgUser.objects.filter(verification_code=verification_code).first()
        if not tg_user:
            raise ValidationError({'verification_code': 'field is incorrect'})
        attrs['tg_user_id'] = tg_user
        return attrs

    # user_id = serializers.CurrentUserDefault
    # tg_id = serializers.IntegerField(source="tg_user_id")
    # username = serializers.CharField(source="tg_username")
    #
    # class Meta:
    #     model = TgUser
    #     fields = ["tg_id", "username", "verification_code", "user_id"]
    #
    # def update(self, instance, validated_data):
    #     instance.user = self.context["request"].user
    #     instance.save()
    #     TgClient(token=settings.BOT_TOKEN).send_message(chat_id=instance.tg_chat_id,
    #                                                     text="✅ Аккаунт успешно подтвержден!\n\n"
    #                                                          "Доступны следующие команды:\n"
    #                                                          "/goals - просмотр целей\n"
    #                                                          "/create - создать цель")
    #     return instance
