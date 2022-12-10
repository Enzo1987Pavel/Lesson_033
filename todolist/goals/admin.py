from django.contrib import admin

from goals.models import GoalCategory, Board

admin.site.site_header = "Модуль 7 SkyPro"
admin.site.site_title = "Диплом"
admin.site.index_title = "Редактирование целей"


class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "updated")
    search_fields = ("title", "user")


admin.site.register(GoalCategory, GoalCategoryAdmin)
admin.site.register(Board)
