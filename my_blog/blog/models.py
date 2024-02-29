from django.db import models


# Создание модели для статей
class Post(models.Model):
    """данные о посте"""
    title = models.CharField('Заголовок записи', max_length=100)  # Хранит поле с текстом длинной N символов
    description = models.TextField('Описание записи', max_length=100)  # Большое текстовое поле не ограниченное количеством знаков
    author = models.CharField('Автор', max_length=100)  # Хранит поле с текстом длинной N символов
    date = models.DateField('Дата публикации')  # Поле хранит дату в виде целого числа в миллисекундах

    def __str__(self):
        """Удобочитаемый вывад полей"""
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'  # Для удобочитаемости в админке
        verbose_name_plural = 'Записи'  # Для удобочитаемости в админке

#
#
#
#
#
#
#
#
