from django.db import models

# Create your models here.


class photos(models.Model):
    photo = models.ImageField(upload_to='img/photos')
    description = models.TextField()

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
