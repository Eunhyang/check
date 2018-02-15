from django.contrib import admin

from note.models import Issue, Memo, Category


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'parent']
    list_filter = ['parent', 'categories']
    filter_horizontal = ['categories']
    list_editable = ['parent']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent']
    list_filter = ['parent']
    list_editable = ['parent']


@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ['id', 'issue', 'content', 'is_base']
    list_filter = ['issue']
