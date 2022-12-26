from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from bot.models import TgUser

from .serializers import BotVerifyCodeUpdateView


class BotVerificationView(generics.UpdateAPIView):
    model = TgUser
    serializer_class = BotVerifyCodeUpdateView
    http_method_names = ["patch"]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(TgUser, verification_code=self.request.data["verification_code"])


    # model = TgUser
    # permission_classess = [IsAuthenticated]
    # # serializer_class = TgUserSerializer
    # http_method_names = ["patch"]
    #
    # queryset = TgUser.objects.all()
    #
    # def patch(self, request, *args, **kwargs):
    #     verif_code = self.request.data.get("verification_code")
    #
    #     if not verif_code:
    #         raise ValidationError({"Указан неверный код проверки!"})
    #
    #     tg_client = TgClient(settings.BOT_TOKEN)
    #     try:
    #         tg_user = TgUser.objects.get(verification_code=verif_code)
    #     except self.model.DoesNotExist:
    #         raise ValidationError({"Не существует пользователя с таким кодом!"})
    #
    #     tg_user.user = self.request.user
    #     tg_user.save()
    #     tg_client.send_message(chat_id=tg_user.tg_chat_id, text=f"✅ Аккаунт подтвержден!!!")
    #     return Response(data=verif_code, status=status.HTTP_201_CREATED)
