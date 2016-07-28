def post_save_url(instance, created, **kwargs):
    import short_url
    import uuid
    from django.conf import settings
    from urlapp.models import Url

    if created:
        instance.short_url = settings.BASE_URL + 's/' + short_url.encode_url(instance.short_id.clock_seq)

        while Url.objects.filter(short_url=instance.short_url).exists():
            instance.short_url = settings.BASE_URL + 's/' + short_url.encode_url(uuid.uuid4().clock_seq)
        instance.save()
