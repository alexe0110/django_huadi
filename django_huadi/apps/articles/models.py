from django.db import models


class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=200)
    article_text = models.TextField('Тест статьи')
    pub_date = models.DateTimeField('Дата публикации')



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # Внешний ключ, для связи между моделями
    author_name = models.CharField('Имя автора', max_length=100)
    comment_text = models.CharField('Текст комментария', max_length=300)
