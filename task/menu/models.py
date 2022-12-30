from django.db import models


class Menu(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название меню'
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'Меню "{self.name}"'


class MenuItem(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название элемента меню'
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='child_items',
        verbose_name='Родитель'
    )
    menu = models.ForeignKey(
        Menu,
        blank=True,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Меню'
    )

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    def __str__(self):
        return (
            f'Элемент: "{self.name}", '
            f'Родитель: {self.parent}, '
            f'Меню: "{self.menu.name}"'
        )
