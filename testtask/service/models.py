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
    

class photo(models.Model):
    id1  = models.IntegerField()
    albumId = models.IntegerField()
    title = models.CharField('title',max_length=100)
    path = models.CharField('path',max_length=100)
    thumbnailUrl = models.CharField('thumbnailUrl',max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'