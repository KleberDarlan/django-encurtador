import uuid
import short_url
from django.db import models
from django.db.models.signals import post_save
from .signals import post_save_url


class Url(models.Model):
    full_url = models.URLField('URL')
    short_url = models.CharField('URL Encurtada', max_length=50, null=True, blank=True)
    short_id = models.UUIDField(default=uuid.uuid4, editable=False)
    counter = models.PositiveIntegerField(
        'Contador', null=False, blank=False, default=0
    )
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.full_url

post_save.connect(
    post_save_url, sender=Url, dispatch_uid='post_save_url'
)
