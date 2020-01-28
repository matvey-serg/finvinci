from django.db import models


class Currency(models.Model):
    short_name = models.CharField(max_length=32)
    value = models.FloatField()

    def __str__(self):
        return self.short_name
