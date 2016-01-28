from django.conf import settings
from django.db import models

#from django_extensions.db.models import TimeStampedModel


class Photo(models.Model):
    app_label = 'photoviewer'

    caption = models.CharField(max_length=200)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=False,
    )

    image = models.ImageField(upload_to='images')
