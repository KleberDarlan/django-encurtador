from django.contrib import admin

from .models import Url


class UrlAdmin(admin.ModelAdmin):

    list_display = [
        'full_url',
        'short_url',
        'counter',
        'created_at'
    ]

admin.site.register(Url, UrlAdmin)
