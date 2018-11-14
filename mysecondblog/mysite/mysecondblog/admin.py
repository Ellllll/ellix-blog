from django.contrib import admin

from models import Article_python,Article_net,Article_personal,Article_deep_learning


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title',)

    class Media:
        js = (
            'js/kindeditor/kindeditor-all.js',
            'js/kindeditor/lang/zh_CN.js',
            'js/kindeditor/config.js',
        )


# Register your models here.
admin.site.register(Article_python, ArticleAdmin)
admin.site.register(Article_net, ArticleAdmin)
admin.site.register(Article_deep_learning, ArticleAdmin)
admin.site.register(Article_personal, ArticleAdmin)

