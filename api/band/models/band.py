from django.db import models


class Band(models.Model):
    """ Band Model """
    name = models.CharField(
        verbose_name='Nome da Banda',
        max_length=100,
        null=False, blank=False
    )
    musicStyle = models.CharField(
        verbose_name='Estilo Musical',
        max_length=150,
        null=False, blank=False
    )
    originLocal = models.CharField(
        verbose_name='Local de Origem',
        max_length=100,
        null=False, blank=False
    )
    formationAt = models.IntegerField(
        verbose_name='Formada em',
        null=False, blank=False
    )

    def __str__(self):
        return f'{self.name} - {self.musicStyle}'
