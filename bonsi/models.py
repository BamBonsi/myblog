from django.conf import settings
from django.db import models
from django.utils import timezone

class Bonsi(models.Model):
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title_name    = models.CharField(max_length=200, default='')
    title_type     = models.CharField(max_length=200, default='')
    title_price     = models.CharField(max_length=100, default='--บาท')
    image = models.ImageField(blank = True)
    text_note = models.TextField(null=True, blank=True)
    created_date    = models.DateTimeField(default=timezone.now, null=True, blank=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title_ru
