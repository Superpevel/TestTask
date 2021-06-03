from django.db import models


class album(models.Model):
    userId = models.IntegerField()
    id  = models.IntegerField(primary_key=True)
    title = models.CharField('title',max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'album'
        verbose_name_plural = 'albums'