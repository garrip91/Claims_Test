from django.db import models
from claims.choices import ClaimTypes

class Claim(models.Model):
    title = models.CharField(verbose_name='Название', max_length=120, default='')
    description = models.TextField(verbose_name='Описание')
    type = models.CharField(
        verbose_name='Тип',
        max_length=120,
        choices=ClaimTypes.choices,
        default=ClaimTypes.COMPUTERS.value
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.title