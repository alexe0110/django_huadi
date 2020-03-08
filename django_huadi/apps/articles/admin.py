from django.contrib import admin

from .models import Article, Comment

# Чтобы было доступно добавление статей в админке
admin.site.register(Article)
admin.site.register(Comment)
