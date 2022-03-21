from django.contrib import admin

from article.models import Tags, Article, Feedback


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added')
    search_fields = ('title',)
    list_filter = ('date_added',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added')
    search_fields = ('text', 'email')
