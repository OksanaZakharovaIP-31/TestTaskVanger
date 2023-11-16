from django.db import models
from filer.fields.image import FilerImageField
# Create your models here.


class slider(models.Model):
    description = models.TextField()
    photo = FilerImageField(null=False, blank=False, related_name='photo_slider', on_delete=models.PROTECT)


    # @property
    # def photo_url(self):
    #     if self.photo and hasattr(self.photo, 'url'):
    #         return self.photo.url
