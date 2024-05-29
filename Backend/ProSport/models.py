from django.db import models


class Items(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='items_images')
    price = models.IntegerField()

    def __str__(self):
        return f'Товар: {self.name}'
