from django.db import models


class NewStats(models.Model):
    objects = None
    win = models.IntegerField()
    mac = models.IntegerField()
    iph = models.IntegerField()
    android = models.IntegerField()
    oth = models.IntegerField()
