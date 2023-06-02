from django.db import models

class Author(models.Model):
    surname = models.CharField('Фамилия', max_length=50)

    class Meta:
        verbose_name = 'Фамилия'
        verbose_name_plural = 'Фамилия' 

class Genre(models.Model):
    name = models.CharField("Жанр", max_length=50)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанр' 

class News(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    text = models.TextField('Статья')
    src = models.CharField('Картинка', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новость'