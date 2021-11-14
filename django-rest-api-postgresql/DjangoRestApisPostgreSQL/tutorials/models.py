from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=80, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)
