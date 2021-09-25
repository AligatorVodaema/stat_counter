from django.db import models



class Statistic(models.Model):
    date = models.DateField(verbose_name='Дата события', blank=False)
    views = models.IntegerField(
        verbose_name='Кол-во показов',
        blank=True,
        null=True
        )
    clicks = models.IntegerField(
        verbose_name='Кол-во кликов',
        blank=True,
        null=True
        )
    cost = models.DecimalField(
        verbose_name='Стоймость кликов',
        blank=True,
        null=True,
        max_digits=8,
        decimal_places=2,
        help_text='Рубли.Копейки'
        )
    cpc = models.DecimalField(
        verbose_name='Средняя стоймость клика',
        blank=True,
        null=True,
        max_digits=8,
        decimal_places=2
        )
    cpm = models.DecimalField(
        verbose_name='Средняя стоймость 1000 показов',
        blank=True,
        null=True,
        max_digits=8,
        decimal_places=2
        )
    
