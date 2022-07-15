from django.db import models

class ClaimTypes(models.TextChoices):
    COMPUTERS = 'Computers', 'Компьютеры'
    NOTEBOOKS = 'Notebooks', 'Ноутбуки'