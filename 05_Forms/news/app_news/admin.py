from django.contrib import admin
from app_news.models import News, Commentary
from django.template.defaultfilters import truncatechars


class NewsInLine(admin.StackedInline):
    model = News
    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self):
        queryset.update(is_active=True)

    def mark_as_inactive(self):
        queryset.update(is_active=False)

    mark_as_active.short_description = 'Перевести в статус Активные'
    mark_as_inactive.short_description = 'Перевести в статус Неактивные'


class CommentaryInLine(admin.TabularInline):
    model = Commentary


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'is_active']
    search_fields = ['title', 'description']
    list_filter = ['created_at', 'is_active']
    inlines = [CommentaryInLine]
    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_as_inactive(self, request, queryset):
        queryset.update(is_active=False)

    mark_as_active.short_description = 'Перевести в статус Активные'
    mark_as_inactive.short_description = 'Перевести в статус Неактивные'


class CommentaryAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'short_comment', 'created_at']
    list_filter = ['news_at', 'user_name']
    actions = ['mark_as_passable', 'mark_as_deletable']

    def mark_as_passable(self, request, queryset):
        pass

    def mark_as_deletable(self, request, queryset):
        queryset.update(comment='Удалено администратором.')

    mark_as_passable.short_description = 'Пропустить комментарий'
    mark_as_deletable.short_description = 'Удалить комментарий'


admin.site.register(News, NewsAdmin)
admin.site.register(Commentary, CommentaryAdmin)
