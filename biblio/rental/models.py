from django.db import models
from django.utils.timezone import now
from django.conf import settings
from shelf.models import BookItem


class Rental(models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    what = models.ForeignKey(BookItem, on_delete=models.CASCADE)
    when = models.DateTimeField(default=now)
    returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.who}, {self.what}, {self.when}'