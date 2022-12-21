from django.conf import settings
from django.core.management.base import BaseCommand

from bot.models import TgUser
from bot.tg.bot_commands import BotGoal
from bot.tg.client import TgClient
from bot.tg.dc import Message


class Command(BaseCommand):
    help = "Runs Telegram bot"
    tg_client = TgClient(settings.BOT_TOKEN)

    def handle_user(self, msg: Message):
        tg_user, created = TgUser.objects.get_or_create(
            tg_user_id=msg.msg_from.id,
            tg_chat_id=msg.chat.id,
        )

        if created:
            tg_user.generate_verification_code()
            self.tg_client.send_message(
                chat_id=msg.chat.id,
                text=f"Для подтверждения аккаунта\n"
                     f"введите код верификации:\n\n"
                     f"{tg_user.verification_code}\n\n"
                     f"на сайте pesaulov87.ga"
            )
        else:
            self.tg_client.send_message(
                chat_id=msg.chat.id,
                text="Вы уже зарегистророваны!"
            )

    def verified_user(self, tg_user, msg: Message):
        if msg.text == '/goals':
            BotGoal(tg_user=tg_user, msg=msg, tg_client=self.tg_client).get_goal()
        elif msg.text == '/start':
            self.tg_client.send_message(
                chat_id=msg.chat.id,
                text=f'Вы уже зарегистророваны!'
            )
        elif 'create' in msg.text:
            BotGoal(tg_user=tg_user, msg=msg, tg_client=self.tg_client).create_goal()
        elif msg.text == '/cancel':
            self.tg_client.send_message(
                chat_id=msg.chat.id,
                text=f'Операция отменена!'
            )
        else:
            self.tg_client.send_message(
                chat_id=msg.chat.id,
                text=f'Неизвестная команда!'
            )

    def add_user(self, msg: Message) -> None:
        tg_user, create = TgUser.objects.get_or_create(
            tg_user_id=msg.msg_from.id,
            tg_chat_id=msg.chat.id,
        )
        if create:
            self.tg_client.send_message(chat_id=msg.chat.id, text='Зарегистрировал вас!')
        if tg_user.user:
            self.verified_user(tg_user=tg_user, msg=msg)
        else:
            BotGoal(tg_user=tg_user, msg=msg, tg_client=self.tg_client).check_user()

    def handle(self, *args, **options):
        offset = 0
        while True:
            res = self.tg_client.get_updates(offset=offset)

            for item in res.result:
                offset = item.update_id + 1
                self.handle_user(item.message)
