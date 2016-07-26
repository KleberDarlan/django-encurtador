import uuid
from django.db import models


class Url(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    full_url = models.URLField('URL')
    counter = models.PositiveIntegerField(
        'Contador', null=False, blank=False, default=0
    )
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.full_url
