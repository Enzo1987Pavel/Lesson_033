from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import TgUser
from .serializers import TgUserSerializer


class BotVerificationView(generics.UpdateAPIView):
    model = TgUser
    permission_classess = [IsAuthenticated]
    serializer_class = TgUserSerializer
    http_method_names = ["patch"]

    def patch(self, request, *args, **kwargs):
        data = self.serializer_class(request.data).data
        tg_user = TgUser.objects.filter(verification_code=data["verification_code"]).first()

        if not tg_user:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        tg_user = request.user
        tg_user.save()
        return Response(data=data, status=status.HTTP_201_CREATED)
