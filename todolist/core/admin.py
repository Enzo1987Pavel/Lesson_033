from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "first_name", "last_name", "email")  # Отображение полей в Админке
    search_fields = ("username", "first_name", "last_name", "email")  # Поиск по полям в Админке
    list_filter = ("is_staff", "is_active", "is_superuser")  # Фильтры по полям в Админке


class PostCodesAdmin(admin.ModelAdmin):
    exclude = ("password",)  # Скрываем поле "Пароль" в Админке
