from django.contrib import admin

from models import Article

class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title',)

    class Media:
        js = (
            'js/kindeditor/kindeditor-all.js',
            'js/kindeditor/lang/zh_CN.js',
            'js/kindeditor/config.js',
        )


# Register your models here.
admin.site.register(Article, ArticleAdmin)

