from django.contrib import admin
from app_news.models import News, Commentary, BlogPost, BlogImage, Offers, Author, Book
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars


class NewsInLine(admin.StackedInline):
    model = News
    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_as_inactive(self, request, queryset):
        queryset.update(is_active=False)

    mark_as_active.short_description = 'Перевести в статус Активные'
    mark_as_inactive.short_description = 'Перевести в статус Неактивные'


class CommentaryInLine(admin.TabularInline):
    model = Commentary


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
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


class BlogAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'created_at']
    list_filter = ['user']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['file']


class OffersAdmin(admin.ModelAdmin):
    list_display = ['user', 'status']
    list_filter = ['user', 'status']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'birth_year']
    list_filter = ['name', 'surname', 'birth_year']


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'release_year', 'page_amount']
    list_filter = ['title', 'isbn', 'release_year', 'page_amount']


admin.site.register(BlogPost, BlogAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Commentary, CommentaryAdmin)
admin.site.register(Offers, OffersAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
