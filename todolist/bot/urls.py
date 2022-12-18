from django.urls import path

from bot.views import TgUserUpdate

urlpatterns = [
    path("verify", TgUserUpdate.as_view(), name="verify"),
]
