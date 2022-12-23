from django.conf import settings
from django.core.management.base import BaseCommand

from bot.models import TgUser
from bot.tg.client import TgClient
from bot.tg.dc import Message
from goals.models import Goal, GoalCategory


class Command(BaseCommand):
    help = "Runs Telegram bot"
    tg_client = TgClient(settings.BOT_TOKEN)

    def choose_categories(self, msg: Message, tg_user: TgUser):
        pass

    def get_categories(self, msg: Message, tg_user: TgUser):
        goal_categories = GoalCategory.objects.filter(
            board__participants__user=tg_user.user,
            is_deleted=False,
        )
        goal_categories_srt = "\n".join(["🔹 " + goal.title for goal in goal_categories])

        self.tg_client.send_message(
            chat_id=msg.chat.id,
            text=f"🏷 Выберите категорию:\n"
                 f"====================\n"
                 f"{goal_categories_srt}:\n"
                 f"====================\n"
        )

    def create_goal(self):
        self.get_categories()
        self.choose_categories()
        #create goal

    def get_goal(self, msg: Message, tg_user: TgUser):
        goals = Goal.objects.filter(category__board__participants__user=tg_user.user).exclude(
            status=Goal.Status.archived)
        goals_str = "\n".join(["🔹 " + goal.title for goal in goals])

        self.tg_client.send_message(
            chat_id=msg.chat.id,
            text=f"📌 Ваш список целей:\n"
                 f"==================\n"
                 f"{goals_str}:\n"
                 f"==================\n"
        )

    def handle_user(self, msg: Message):
        tg_user, created = TgUser.objects.get_or_create(
            tg_user_id=msg.msg_from.id,
            tg_chat_id=msg.chat.id,
            tg_username=msg.chat.username,
        )

        if created:
            tg_user.generate_verification_code()
            self.tg_client.send_message(
                chat_id=msg.chat.id,
                text=f"Для подтверждения аккаунта\n"
                     f"введите код проверки:\n\n"
                     f"{tg_user.verification_code}\n\n"
                     f"на сайте pesaulov87.ga"
            )
        elif msg.text == "/goals":
            self.get_goal(msg, tg_user)

        elif msg.text == "/create":
            pass

        else:
            self.tg_client.send_message(
                chat_id=msg.chat.id,
                text=f"⛔ Вы ввели неизвестную команду ( **{msg.text}** )!"
            )

        # else:
        #     self.tg_client.send_message(
        #         chat_id=msg.chat.id,
        #         text="Ваш аккаунт уже был подтвержден!"
        #     )

    def handle(self, *args, **options):
        offset = 0
        while True:
            res = self.tg_client.get_updates(offset=offset)

            for item in res.result:
                offset = item.update_id + 1
                self.handle_user(item.message)
